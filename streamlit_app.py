import streamlit as st
import pandas as pd
import openpyxl
import numpy as np
import plotly.express as px

# Activate conda environment
#conda create -n <envName> python=3.10
#conda activate <envName>
#conda env list
#conda env remove -n <envName>
#streamlit run streamlit_app.py


st.title("Patent Scope Data")
# Upload XLSX data
with st.sidebar.header('File Input'):
    uploaded_file = st.sidebar.file_uploader("Upload your .XLSX file", type=["xlsx"])
    
# Pandas Profiling Report
if uploaded_file is not None:
    st.info('XLSX file is uploaded.')

else:
    st.info('Awaiting for XLSX file to be uploaded.')

