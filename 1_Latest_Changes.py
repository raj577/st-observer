import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Baro",
    page_icon="👋",
)
st.write("Developed by rajat aka TheChartsCruncher")

uploaded_file = st.file_uploader("Upload Files",type=['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    
    df = df[df['OPEN_INT'] > 0]
    #df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
    	
   
    metadata = df
        
    option = st.sidebar.selectbox(
        'Symbol',
        metadata['SYMBOL'].unique())
    
    option_exp = st.sidebar.selectbox(
            'Expiry DATE',
            metadata['EXPIRY_DT'].unique())
    
    
    option_inst = st.sidebar.selectbox(
        'INSTRUMENT',
        metadata['INSTRUMENT'].unique())

     
    option_date = st.sidebar.selectbox(
        'Date',
        metadata['TIMESTAMP'].unique())
    
    
    filterdata = metadata[(metadata['SYMBOL'] == option) & (metadata['EXPIRY_DT'] == option_exp) & (metadata['INSTRUMENT'] == option_inst) & (metadata['TIMESTAMP'] == option_date)]
    


    
    
    
    
    
    oi_chart = px.bar(
            filterdata, 
            x='STRIKE_PR',
            y='OPEN_INT',barmode='group',color='OPTION_TYP',
                        color_discrete_map={
                'PE': 'red',
                'CE': 'green'
            },
            height=500,width=1300
        )

    st.plotly_chart(oi_chart)

    coi_chart = px.bar(
            filterdata, 
            x='STRIKE_PR',
            y='CHG_IN_OI',barmode='group',color='OPTION_TYP',
                        color_discrete_map={
                'PE': 'red',
                'CE': 'green'
            },
            height=500,width=1500
        )

    st.plotly_chart(coi_chart)
    
    st.dataframe(filterdata)






























elif uploaded_file is  None:
    


    df = pd.read_csv("jandta.csv")
    df = df[df['OPEN_INT'] > 0]
    #df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
    	
   
    metadata = df
        
    option = st.sidebar.selectbox(
        'Symbol',
        metadata['SYMBOL'].unique())
    
    option_exp = st.sidebar.selectbox(
            'Expiry DATE',
            metadata['EXPIRY_DT'].unique())
    
    
    option_inst = st.sidebar.selectbox(
        'INSTRUMENT',
        metadata['INSTRUMENT'].unique())

     
    option_date = st.sidebar.selectbox(
        'Date',
        metadata['TIMESTAMP'].unique())
    
    
    filterdata = metadata[(metadata['SYMBOL'] == option) & (metadata['EXPIRY_DT'] == option_exp) & (metadata['INSTRUMENT'] == option_inst) & (metadata['TIMESTAMP'] == option_date)]
    


    
    
    
    
    oi_chart = px.bar(
            filterdata, 
            x='STRIKE_PR',
            y='OPEN_INT',barmode='group',color='OPTION_TYP',
                        color_discrete_map={
                'PE': 'red',
                'CE': 'green'
            },
            height=500,width=1300
        )

    st.plotly_chart(oi_chart)

    coi_chart = px.bar(
            filterdata, 
            x='STRIKE_PR',
            y='CHG_IN_OI',barmode='group',color='OPTION_TYP',
                        color_discrete_map={
                'PE': 'red',
                'CE': 'green'
            },
            height=500,width=1500
        )

    st.plotly_chart(coi_chart)
    
    st.dataframe(filterdata) 



st.write("Developed by rajat aka TheChartsCruncher")







