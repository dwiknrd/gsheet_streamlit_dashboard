import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import time

st.set_page_config(page_title='Data Profiler', layout='wide', page_icon='📝')

st.markdown("<h1 style='text-align: center;'>📑 Data Report</h1>", unsafe_allow_html=True)
st.markdown("---")

# Initialize session state for df and report if not already done
if 'df' not in st.session_state:
    st.session_state.df = None
if 'report' not in st.session_state:
    st.session_state.report = None

# Function to read data from Google Sheets and cache it
@st.cache_data(ttl=3600)  # Cache data for 1 hour
def load_data(spreadsheet_id, worksheet_id):
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(
        spreadsheet=spreadsheet_id,
        worksheet=worksheet_id,
        ttl=0
    )
    return df

# Function to generate profile report and cache it
@st.cache_data(ttl=3600)  # Cache report for 1 hour
def generate_report(df):
    return ProfileReport(df)

if st.sidebar.button("Start Profiling Data"):
    spreadsheet_id = st.secrets.data_tips["spreadsheet2"]
    worksheet_id = "773835363"

    df = load_data(spreadsheet_id, worksheet_id)

    # Save the dataframe in session state
    st.session_state.df = df

    # Placeholder for progress bar
    progress_bar = st.sidebar.progress(0)
    progress_text = st.sidebar.empty()

    # Generate the report and save it in session state
    with st.spinner('Generating Report ⏳⌛⏳⌛⏳⌛'):
        for percent_complete in range(100):
            time.sleep(0.1)
            progress_bar.progress(percent_complete + 1)
            progress_text.text(f'⏳⌛ {percent_complete + 1}% Complete')

        report = generate_report(df)
        st.session_state.report = report

    st_profile_report(st.session_state.report)

else:
    st.info('Click button in the left sidebar to generate data report')

# Display the report if it exists in the session state
if st.session_state.report is not None:
    st_profile_report(st.session_state.report, key="profile_report_main_existing")


# import streamlit as st
# from streamlit_gsheets import GSheetsConnection

# import pandas as pd 
# from ydata_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report
# import time


# st.set_page_config(page_title='Data Profiler',layout='wide', page_icon='📝')


# st.markdown("<h1 style='text-align: center;'>📑 Data Report</h1>", unsafe_allow_html=True)

# st.markdown("---")

# # Initialize session state for df and report if not already done



# if st.sidebar.button("Start Profiling Data"):
#     # Create a connection object.
#     conn = st.connection("gsheets", type=GSheetsConnection)

#     df = conn.read(
#         spreadsheet = st.secrets.data_tips["spreadsheet2"],
#         worksheet="773835363", # nama worksheet yang ingin diambil
#         ttl=0
#     )

#     # Placeholder for progress bar
#     progress_bar = st.sidebar.progress(0)
#     progress_text = st.sidebar.empty()


#     # Print results.
#     with st.spinner('Generating Report ⏳⌛⏳⌛⏳⌛'):
#         for percent_complete in range(100):
#             time.sleep(0.1)
#             progress_bar.progress(percent_complete + 1)
#             progress_text.text(f'⏳⌛ {percent_complete + 1}% Complete')

#         pr = ProfileReport(df)

#     st_profile_report(pr)
    
# else:
#     st.info('Click button in the left sidebar to generate data report')

# Footer
footer_content = """
---

© 2024 Dwi Gustin Nurdialit
"""
st.markdown(f"<h1 style='text-align: center;'>{footer_content}</h1>", unsafe_allow_html=True)