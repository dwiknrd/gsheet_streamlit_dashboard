import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import os
import sys
import base64

# Configurasi halaman
st.set_page_config(page_title='Data Profiler', layout='wide', page_icon='📝')

# Judul halaman
st.markdown("<h1 style='text-align: center;'>📤 Upload Your Data</h1>", unsafe_allow_html=True)
st.markdown("---")

# Fungsi untuk mendapatkan ukuran file
def get_filesize(file):
    size_bytes = sys.getsizeof(file)
    size_mb = size_bytes / (1024**2)
    return size_mb

# Fungsi untuk validasi file
def validate_file(file):
    _, ext = os.path.splitext(file.name)
    return ext if ext in ('.csv', '.xlsx') else False

# Fungsi untuk menghasilkan laporan
@st.cache_data
def generate_report(df):
    return ProfileReport(df)

# Inisialisasi session state
if 'df' not in st.session_state:
    st.session_state.df = None
if 'report' not in st.session_state:
    st.session_state.report = None

# Sidebar untuk mengunggah file
with st.sidebar:
    uploaded_file = st.file_uploader("Upload .csv, .xlsx files not exceeding 10 MB")

if uploaded_file is not None:
    ext = validate_file(uploaded_file)
    if ext:
        filesize = get_filesize(uploaded_file)
        if filesize <= 10:
            if ext == '.csv':
                df = pd.read_csv(uploaded_file)
            else:
                xl_file = pd.ExcelFile(uploaded_file)
                sheet_name = st.sidebar.selectbox('Select the sheet', xl_file.sheet_names)
                df = xl_file.parse(sheet_name)

            # Simpan dataframe dan laporan dalam session state
            st.session_state.df = df
            st.session_state.report = generate_report(df)

            # Tampilkan laporan di halaman utama
            st_profile_report(st.session_state.report)

            # Tombol unduh untuk laporan HTML
            html_report_str = st.session_state.report.to_html()
            b64 = base64.b64encode(html_report_str.encode()).decode()
            href = f'<a href="data:text/html;base64,{b64}" download="report.html">Click here to download report</a>'
            st.sidebar.markdown(href, unsafe_allow_html=True)
        else:
            st.error(f'Maximum allowed filesize is 10 MB. But received {filesize:.2f} MB')
    else:
        st.error('Kindly upload only .csv or .xlsx file')
else:
    st.info('Upload your data in the left sidebar to generate profiling')

# Tampilkan laporan jika sudah ada dalam session state
if st.session_state.report is not None:
    st_profile_report(st.session_state.report)

    # Tombol unduh untuk laporan HTML di sidebar
    html_report_str = st.session_state.report.to_html()
    b64 = base64.b64encode(html_report_str.encode()).decode()
    href = f'<a href="data:text/html;base64,{b64}" download="report.html">Click here to download report</a>'
    st.sidebar.markdown(href, unsafe_allow_html=True)


# Footer
footer_content = """
---

© 2024 Dwi Gustin Nurdialit
"""
st.markdown(f"<h1 style='text-align: center;'>{footer_content}</h1>", unsafe_allow_html=True)