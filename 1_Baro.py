import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import jugaad_data as jd
from jugaad_data.nse import NSELive

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
    


    # n = NSELive()
    # q = n.stock_quote(option)
    #st.write("Current price" , q['priceInfo']['lastPrice'])
    
    # st.write(option, q['priceInfo']['lastPrice'])
    
    
    
    
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







# import streamlit as st
# import numpy as np
# import pandas as pd
# import plotly.express as px
# import jugaad_data as jd
# from jugaad_data.nse import NSELive
# import datetime
# my_date = datetime.date(2022, 12, 2)

# st.set_page_config(
#     page_title="Baro",
#     page_icon="👋",
# )
# st.write("Developed by rajat aka thecruncher")
# uploaded_file = st.file_uploader("Upload Files",type=['csv'])
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
    
#     df = df[df['OPEN_INT'] > 0]
    
    	
   
#     metadata = df
   
        
#     option = st.sidebar.selectbox(
#         'Symbol',
#         metadata['SYMBOL'].unique())
    
#     option_exp = st.sidebar.selectbox(
#             'Expiry DATE',
#             metadata['EXPIRY_DT'].unique())
    
    
#     option_inst = st.sidebar.selectbox(
#         'INSTRUMENT',
#         metadata['INSTRUMENT'].unique())

     
#     option_t = st.sidebar.selectbox(
#         'TIMESTAMP',
#         metadata['TIMESTAMP'].unique())
    
    
    
    
#     filterdata = metadata[(metadata['SYMBOL'] == option) & (metadata['EXPIRY_DT'] == option_exp) & (metadata['INSTRUMENT'] == option_inst) & (metadata['TIMESTAMP']) == option_t]
    


#     n = NSELive()
#     q = n.stock_quote(option)
#     #st.write("Current price" , q['priceInfo']['lastPrice'])
    
    
    
    
    
    
#     oi_chart = px.bar(
#             filterdata, 
#             x='STRIKE_PR',
#             y='OPEN_INT',barmode='group',
#             color='OPTION_TYP',
            # color_discrete_map={
            #     'PE': 'red',
            #     'CE': 'green'
            # },
#             height=500,
#             width=1300
#         )

#     st.plotly_chart(oi_chart)
#     st.write(option, q['priceInfo']['lastPrice'], "previous close" ,q['priceInfo']['previousClose'])
    
#     coi_chart = px.bar(
#             filterdata, 
#             x='STRIKE_PR',
#             y='CHG_IN_OI',barmode='group',color='OPTION_TYP',
#             color_discrete_map={
#                 'PE': 'red',
#                 'CE': 'green'
#             },
#             height=500,width=1500,
#             text='STRIKE_PR'
#         )

#     st.plotly_chart(coi_chart)
    
#     st.dataframe(filterdata)
    


#     st.write("Developed by rajat aka thecruncher")