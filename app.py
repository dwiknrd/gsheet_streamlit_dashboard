import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(
    spreadsheet = st.secrets.data_tips["spreadsheet2"],
    worksheet="773835363", # nama worksheet yang ingin diambil
    ttl=0,
    usecols=[0, 1],
    nrows=3,
)


# Print results.
st.dataframe(df.head())