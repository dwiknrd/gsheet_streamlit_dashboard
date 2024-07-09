import streamlit as st
from streamlit_gsheets import GSheetsConnection

import pandas as pd 
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import time

import os
import sys
import base64

st.set_page_config(page_title='Data Profiler',layout='wide', page_icon='📝')


st.markdown("<h1 style='text-align: center;'>📤 Upload Your Data</h1>", unsafe_allow_html=True)
st.markdown("---")


def get_filesize(file):
    size_bytes = sys.getsizeof(file)
    size_mb = size_bytes / (1024**2)
    return size_mb

def validate_file(file):
    filename = file.name
    name, ext = os.path.splitext(filename)
    if ext in ('.csv','.xlsx'):
        return ext
    else:
        return False
    

# Function to generate profile report
def generate_report(df):
    with st.spinner('Generating Report'):
        pr = ProfileReport(df)
    return pr

# Initialize session state for df and report if not already done
if 'df' not in st.session_state:
    st.session_state.df = None
if 'report' not in st.session_state:
    st.session_state.report = None
    

# sidebar
with st.sidebar:
    uploaded_file = st.file_uploader("Upload .csv, .xlsx files not exceeding 10 MB")
        
    
if uploaded_file is not None:
    ext = validate_file(uploaded_file)
    if ext:
        filesize = get_filesize(uploaded_file)
        if filesize <= 10:
            if ext == '.csv':
                # time being let load csv
                df = pd.read_csv(uploaded_file)
            else:
                xl_file = pd.ExcelFile(uploaded_file)
                sheet_tuple = tuple(xl_file.sheet_names)
                sheet_name = st.sidebar.selectbox('Select the sheet',sheet_tuple)
                df = xl_file.parse(sheet_name)

            # Save the dataframe in session state
            st.session_state.df = df

            # Generate and save the report in session state
            st.session_state.report = generate_report(df)

            # Display the report in the main page
            st_profile_report(st.session_state.report)    

            # Download button for HTML report
            html_report_str = st.session_state.report.to_html()
            b64 = base64.b64encode(html_report_str.encode()).decode()
            href = f'<a href="data:text/html;base64,{b64}" download="report.html">Click here to download report</a>'
            st.sidebar.markdown(href, unsafe_allow_html=True)

        else:
            st.error(f'Maximum allowed filesize is 10 MB. But received {filesize} MB')
            
    else:
        st.error('Kindly upload only .csv or .xlsx file')
        
else:
    st.info('Upload your data in the left sidebar to generate profiling')
    
# Display the report if it exists in the session state
if st.session_state.report is not None:
    st_profile_report(st.session_state.report, key="profile_report_main_existing")

    # # Download button for HTML report in sidebar
    # html_report_str = st.session_state.report.to_html()
    # b64 = base64.b64encode(html_report_str.encode()).decode()
    # href = f'<a href="data:text/html;base64,{b64}" download="report.html">Click here to download report</a>'
    # st.sidebar.markdown(href, unsafe_allow_html=True)