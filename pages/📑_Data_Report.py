import streamlit as st
from streamlit_gsheets import GSheetsConnection

import pandas as pd 
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import time


st.set_page_config(page_title='Data Profiler',layout='wide', page_icon='📝')


st.markdown("<h1 style='text-align: center;'>📑 Data Report</h1>", unsafe_allow_html=True)

st.markdown("---")


# with st.sidebar:
#     st.subheader("Spreadsheet Data")
#     st.markdown("---")


if st.sidebar.button("Start Profiling Data"):
    # Create a connection object.
    conn = st.connection("gsheets", type=GSheetsConnection)

    df = conn.read(
        spreadsheet = st.secrets.data_tips["spreadsheet2"],
        worksheet="773835363", # nama worksheet yang ingin diambil
        ttl=0
    )

    # Placeholder for progress bar
    progress_bar = st.sidebar.progress(0)
    progress_text = st.sidebar.empty()


    # Print results.
    with st.spinner('Generating Report ⏳⌛⏳⌛⏳⌛'):
        for percent_complete in range(100):
            time.sleep(0.1)
            progress_bar.progress(percent_complete + 1)
            progress_text.text(f'⏳⌛ {percent_complete + 1}% Complete')

        pr = ProfileReport(df)

    st_profile_report(pr)
    
else:
    st.info('Click button in the left sidebar to generate data report')
