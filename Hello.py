import streamlit as st
# from streamlit_carousel import carousel


# Konten halaman About dalam format Markdown
about_content = """
#### About This Application

Welcome to our dynamic data dashboard application! This tool is designed to generate detailed reports from dynamic datasets, ensuring you always have the latest insights at your fingertips.

#### Key Features

1. **Data Profiling**
   - Presents data profiling reports using ydata-profiling, a tool for analyzing and visualizing dataset characteristics.

2. **Dynamically Updated**
   - Dynamically updates data, integrated with Google Spreadsheet data to ensure information is always up-to-date.

3. **Upload Your Data**
   - Upload your data to generate instant downloadable reports, facilitating quick and efficient analysis.

#### Contact Us

If you have any questions, suggestions, or feedback, feel free to reach out to us at [dwiknrd@gmail.com](mailto:dwiknrd@gmail.com).

---

Thank you for using our application!
"""

st.set_page_config(page_title='Data Profiler',
                   layout='wide', 
                   page_icon='📝', 
                   initial_sidebar_state= "collapsed",
                   menu_items={
                        'About': about_content
    })


st.markdown("<h1 style='text-align: center;'>Data Profiler App</h1>", unsafe_allow_html=True)

st.markdown("---")


# test_items = [
#     dict(
#         title="Data Profiling",
#         text="Presents data profiling reports using ydata-profiling, a tool for analyzing and visualizing dataset characteristics.",
#         img="https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1415&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#     ),
#     dict(
#         title="Dynamically Updated",
#         text="Dynamically updated data, integrated with Google Spreadsheet data to ensure information is always up-to-date.",
#         img="https://plus.unsplash.com/premium_photo-1661881801573-6506e682cbd6?q=80&w=1429&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#     ),
#     dict(
#         title="Upload Your Data",
#         text="Upload data to generate instant downloadable reports, facilitating quick and efficient analysis.",
#         img="https://plus.unsplash.com/premium_photo-1677093905912-a653c6301260?q=80&w=1632&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#     ),
# ]

# carousel(items=test_items, width=0.8)


# Footer
footer_content = """
---

© 2024 Dwi Gustin Nurdialit
"""
st.markdown(f"<h1 style='text-align: center;'>{footer_content}</h1>", unsafe_allow_html=True)
