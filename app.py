import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(
    worksheet="tips", # nama worksheet yang ingin diambil
    ttl="10m" # waktu cache
)

# Print results.
st.write(df)