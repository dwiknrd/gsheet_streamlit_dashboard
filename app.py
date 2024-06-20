import streamlit as st
from streamlit_gsheets import GSheetsConnection

import pandas as pd 
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import time

st.set_page_config(page_title='Data Profiler',layout='wide', page_icon='📝')


st.title("📝 Data Profiler")

with st.sidebar:
    st.subheader("Spreadsheet Data")
    st.markdown("---")


if st.sidebar.button("Start Profiling Data"):
    # Create a connection object.
    conn = st.connection("gsheets", type=GSheetsConnection)

    df = conn.read(
        spreadsheet = st.secrets.data_tips["spreadsheet2"],
        worksheet="773835363", # nama worksheet yang ingin diambil
        ttl=0
    )


    # Print results.
    with st.spinner('Generating Report ⏳⌛⏳⌛⏳⌛'):
        pr = ProfileReport(df)
        time.sleep(3)

    st_profile_report(pr)
    
else:
    st.sidebar.write("👆👆 Click to see magic 🪄")
