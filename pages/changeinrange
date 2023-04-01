import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


st.set_page_config(page_title="Plotting Demo", page_icon="📈")
st.write("Developed by rajat aka TheChartsCruncher")
uploaded_file = st.file_uploader("Upload Files",type=['csv'])




# tab1, tab2, tab3 = st.tabs(["ju", "uui", "hhghvc"])

# with tab1:
#    st.header("A gukhk")
#    st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fgroww.in%2Fblog%2Fhow-to-read-candlestick-charts&psig=AOvVaw0_kH1N0YR9v9zySKzIPFe8&ust=1673603758357000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCKjzzf3hwfwCFQAAAAAdAAAAABAJ", width=200)

# with tab2:
#    st.header("A bhjhg")
#    st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fgroww.in%2Fblog%2Fhow-to-read-candlestick-charts&psig=AOvVaw0_kH1N0YR9v9zySKzIPFe8&ust=1673603758357000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCKjzzf3hwfwCFQAAAAAdAAAAABAJ", width=200)

# with tab3:
#    st.header("hjhgh")
#    st.image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fgroww.in%2Fblog%2Fhow-to-read-candlestick-charts&psig=AOvVaw0_kH1N0YR9v9zySKzIPFe8&ust=1673603758357000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCKjzzf3hwfwCFQAAAAAdAAAAABAJ", width=200)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    
    df = df[df['OPEN_INT'] > 0]
    #df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
    	
   
    metadata = df
        
    option = st.sidebar.selectbox(
        'Symbol',
        metadata['SYMBOL'].unique(),index=5)
    
    option_exp = st.sidebar.selectbox(
            'Expiry DATE',
            metadata['EXPIRY_DT'].unique())
    
    
    option_inst = st.sidebar.selectbox(
        'INSTRUMENT',
        metadata['INSTRUMENT'].unique(),index = 3)

     
    option_dt1 = st.sidebar.selectbox(
        'Date1',
        metadata['TIMESTAMP'].unique())
    
    option_dt2 = st.sidebar.selectbox(
        'Date2',
        metadata['TIMESTAMP'].unique())
    
    option_dt3 = st.sidebar.selectbox(
        'Date3',
        metadata['TIMESTAMP'].unique())
    
    df_strikeprice = metadata[(metadata['SYMBOL'] == option) & (metadata['EXPIRY_DT'] == option_exp) & (metadata['INSTRUMENT'] == option_inst)]
    option_st = st.sidebar.selectbox(
        'STRIKE PRICE',
      df_strikeprice['STRIKE_PR'].unique())
    
    filterdata_dt1 = metadata[(metadata['SYMBOL'] == option) & (metadata['EXPIRY_DT'] == option_exp) & (metadata['INSTRUMENT'] == option_inst) & (metadata['TIMESTAMP'] == option_dt1)]

    filterdata_dt2 = metadata[(metadata['SYMBOL'] == option) & (metadata['EXPIRY_DT'] == option_exp) & (metadata['INSTRUMENT'] == option_inst) & (metadata['TIMESTAMP'] == option_dt2)]

    filterdata_dt3 = metadata[(metadata['SYMBOL'] == option) & (metadata['EXPIRY_DT'] == option_exp) & (metadata['INSTRUMENT'] == option_inst) & (metadata['TIMESTAMP'] == option_dt3)]
    


    # n = NSELive()
    # q = n.stock_quote(option)
    #st.write("Current price" , q['priceInfo']['lastPrice'])
    
    # st.write(option, q['priceInfo']['lastPrice'])
    
    
    
    
    # oi_chart = px.bar(
    #         filterdata_dt1, 
    #         x='STRIKE_PR',
    #         y='OPEN_INT',barmode='group',color='OPTION_TYP',
    #                     color_discrete_map={
    #             'PE': 'red',
    #             'CE': 'green'
    #         },
    #         height=500,width=1300
    #     )

    # st.plotly_chart(oi_chart)
#date 1 --------->
    #st.write(filterdata_dt1['TIMESTAMP'].unique())
    
    coi_chart_dt1 = px.bar(
            filterdata_dt1, 
            x='STRIKE_PR',
            
            y='CHG_IN_OI',barmode='group',color='OPTION_TYP',
                        color_discrete_map={
                'PE': 'red',
                'CE': 'green'
            },
            
            height=300,width=1000
        )

    st.plotly_chart(coi_chart_dt1)
    
    # st.dataframe(filterdata_dt1)

#date 2 --------->

    coi_chart_dt2 = px.bar(
            filterdata_dt2, 
            x='STRIKE_PR',
            y='CHG_IN_OI',barmode='group',color='OPTION_TYP',
                        color_discrete_map={
                'PE': 'red',
                'CE': 'green'
            },
            height=300,width=1500
        )

    st.plotly_chart(coi_chart_dt2)
    
    # st.dataframe(filterdata_dt1)
    
 #date 3 --------->
    
    coi_chart_dt3 = px.bar(
            filterdata_dt3, 
            x='STRIKE_PR',
            #text= filterdata_dt3['STRIKE_PR'],
            y='CHG_IN_OI',barmode='group',color='OPTION_TYP',
                        color_discrete_map={
                'PE': 'red',
                'CE': 'green'
            },
            height=300,width=1500
        )

    st.plotly_chart(coi_chart_dt3)
    fign = make_subplots(specs=[[{"secondary_y": True}]])
    st.write("Developed by rajat aka TheChartsCruncher")
    df_specificstce = df_strikeprice[(df_strikeprice['STRIKE_PR']== option_st) & (df_strikeprice['OPTION_TYP'] == 'CE') ]
    df_specificstpe = df_strikeprice[(df_strikeprice['STRIKE_PR']== option_st) & (df_strikeprice['OPTION_TYP'] == 'PE') ]
    
    fign.add_trace(
   
    go.Scatter(x=df_specificstce['TIMESTAMP'], y=df_specificstce["CHG_IN_OI"], name="CE change",marker={'color': 'green'}),
    secondary_y=False,)
    
    fign.add_trace(
    
    go.Scatter(x=df_specificstce['TIMESTAMP'], y=df_specificstpe["CHG_IN_OI"], name="PE change",marker={'color': 'red'}),
    secondary_y=True,)


#    fig.update_layout(
#     title_text="Double Y Axis Example"
#    )
                       
    # fig = px.line(df_specificstce, x='TIMESTAMP', y="CHG_IN_OI",text=df_specificstce['CHG_IN_OI'])
    # figp = px.line(df_specificstpe, x='TIMESTAMP', y="CHG_IN_OI")
    # st.plotly_chart(fig)
    # st.plotly_chart(figp)
    fign.update_yaxes(title_text="<b>CE change</b>", secondary_y=False)
    fign.update_yaxes(title_text="<b>PE change</b>", secondary_y=True)
    st.plotly_chart(fign)
    
    # st.dataframe(filterdata_dt1)
    # st.dataframe(filterdata_dt2)
    # st.dataframe(filterdata_dt3)
    st.dataframe(df_specificstce)
    st.dataframe(df_specificstpe)








