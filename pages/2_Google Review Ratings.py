import streamlit as st
import pandas as pd
import openpyxl
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Activate conda environment
#conda create -n <envName> python=3.10
#conda activate <envName>
#conda env list
#conda env remove -n <envName>

#streamlit run streamlit_app.py



# TEST FILE 
# All Highlands Coffee Reviews Final.xlsx
# Take 10 seconds to upload 70k rows of date in excel file

st.title("Patent Scope Data")

# Upload XLSX data
with st.sidebar.header('File Input'):
    uploaded_file = st.sidebar.file_uploader("Upload your .XLSX file", type=["xlsx"])
    

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_excel():
        combined_Count = pd.DataFrame()
        combined_Rating = pd.DataFrame()
        headers = []
        files = [uploaded_file]

        for file in files:
            companyName = 'Highlands Coffee'
            headers.append(companyName)
            df_1 = pd.read_excel(file)
            df_2 = df_1.groupby(df_1['date'].dt.year)['stars'].count()
            df_3 = df_1.groupby(df_1['date'].dt.year)['stars'].mean()
            combined_Count = pd.concat([combined_Count, df_2], axis='columns')
            combined_Rating = pd.concat([combined_Rating, df_3], axis='columns')

        countHeaders = [x + " Count" for x in headers]
        ratingHeaders = [x + " Ratings" for x in headers]
        combined_Count.columns = countHeaders
        combined_Rating.columns = ratingHeaders

        combined_df = pd.concat([combined_Count, combined_Rating], axis=1)
        

        return combined_df

    
    st.write(uploaded_file.name)
    df = load_excel()
    st.header('**Google Reviews Ratings Data**')
    st.write('Total number of Inventors:', len(df.columns))
    st.write(df)


    st.write('---')
    st.header('**Google Reviews Ratings Chart**')
    df_2 = df


    fig = make_subplots(specs=[[{"secondary_y": True}]])
    # Add traces
    fig.add_trace(
        go.Line(x=df_2.index, y=df_2['Highlands Coffee Ratings'], name='Highlands Coffee Ratings'),
        secondary_y=True,
    )

    fig.add_trace(
        go.Bar(x=df_2.index, y=df_2['Highlands Coffee Count'], name="Highlands Coffee Count"),
        secondary_y=False,
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Year")
    # Set y-axes titles
    fig.update_yaxes(title_text="Rating", secondary_y=False)
    fig.update_yaxes(title_text="Number of Reviews", secondary_y=True)
    fig.update_layout(height=800, width=1500)

    st.plotly_chart(fig)


else:
    st.info('Awaiting for CSV file to be uploaded.')

