"""
Authors: Rahul, Akshay, Abhishek, Ferdi
Usages: Via stremlit application
Prototype: Hybrid Working Model
"""

# Import labraries
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from prophet  import Prophet
from google.cloud import bigquery
import os
import datetime
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from prophet.plot import plot_plotly, plot_components_plotly



PROJECT = 'hack-team-botarmy' # REPLACE WITH YOUR PROJECT NAME 
REGION = 'us-central-1' # REPLACE WITH YOUR REGION e.g. us-central1

#Don't change the following command - this is to check if you have changed the project name above.
assert PROJECT != 'your-project-name', 'Don''t forget to change the project variables!'


#Streamlit Setup
st.set_page_config(
    page_title="Hybrid Working Model Impact analysis and Prediction",
    page_icon='🎈',
    layout="wide",
    initial_sidebar_state="expanded")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                content:'copyrights © 2021 BOT ARMY';
                visibility: visible;
                display: block;
                position: relative;
                #background-color: red;
                padding: 10px;
                top: 12px;
            }
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)


st.sidebar.title("Bot Army `ʕ•́ᴥ•̀ʔ`")
st.sidebar.write("---")
st.sidebar.write("")

st.sidebar.write(
f"""
## Dataset Used
- **Employee Swipe-IN Swipe-Out**
- **MoveInSync**
- **Vendor transaction**
""")

st.sidebar.write("")

st.sidebar.write(
f"""
## This app is maintained by:
- **Akshay Dhote**
- **Ferdinand Manuel**
- **Abhishek Ranjan**
- **Rahul Kumeriya**
"""
)
st.sidebar.button("For Demo purpose only")

st.title("Hybrid Workplace Management Systsm [HWMS]")


# Load data for bigquery
# Construct a BigQuery client object.
client = bigquery.Client()

# Querying a subset of the table
sql_query = ("""SELECT 
  *
FROM 
  `bot_army.emp_data`
""")

# Storing the data in a pandas DataFrame
employee_df = client.query(sql_query).to_dataframe()


# Querying a subset of the table
sql_query = ("""SELECT 
  *
FROM 
  `bot_army.move_in_sync`
""")

# Storing the data in a pandas DataFrame
comute_df = client.query(sql_query).to_dataframe()


# Querying a subset of the table
sql_query = ("""SELECT 
  *
FROM 
  `bot_army.vendor`
""")

# Storing the data in a pandas DataFrame
vendor_df = client.query(sql_query).to_dataframe()

###########################
# Cleaning data employee data
###########################
# Convert to pandas datetime format
employee_df['Swipe_In']=pd.to_datetime(employee_df['Swipe_In'],  format='%d-%m-%Y %H:%M')
employee_df['Swipe_Out']=pd.to_datetime(employee_df['Swipe_Out'],  format='%d-%m-%Y %H:%M')
new_df = employee_df
# Clean data 
new_df = new_df.loc[:, ~new_df.columns.str.contains('^string_field')]
new_df.drop(columns=['day'], inplace=True)
new_df['dayofweek'] = new_df['Swipe_In'].dt.dayofweek
# map the day of the week number to its name
new_df['dayofweek'] = new_df['dayofweek'].map({
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
})

new_df['Year'] = new_df.Swipe_In.dt.year
new_df['Month'] = new_df.Swipe_In.dt.month
# Considering Swipe_in date as working date
new_df['Working_Date'] = new_df['Swipe_In'].dt.date


num_of_emp_df = new_df['EMP_ID'].groupby([new_df.Working_Date]).agg('count')
st.write("")
st.subheader("🎈 Employee Distrubution over time")
a = pd.DataFrame(num_of_emp_df)
a.rename(columns={'EMP_ID':'Employee Count','Working_Date':'Date'}, inplace=True)
st.bar_chart(a)

###########################
# Cleaning Vendor data
###########################
# Convert to pandas datetime format

vendor_df['Date']=pd.to_datetime(vendor_df['Date'],  format='%d-%m-%Y %H:%M')

vendor_df['dayofweek'] = vendor_df['Date'].dt.dayofweek
# map the day of the week number to its name
vendor_df['dayofweek'] = vendor_df['dayofweek'].map({
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
})
vendor_df = vendor_df.loc[:, ~vendor_df.columns.str.contains('^string_field')]
vendor_df.drop(columns=['day'], inplace=True)
vendor_df['Transaction_Date'] = vendor_df['Date'].dt.date
st.write("")
st.subheader("🎈 Vendor Transactions over time")
num_of_trans_df = vendor_df['Transaction_Value'].groupby([vendor_df.Transaction_Date]).agg('count')
b = pd.DataFrame(num_of_trans_df)
b.rename(columns={'Transaction_Value':'Transactions Count','Transaction_Date':'Date'}, inplace=True)
st.bar_chart(b)

    
#################################
# Forecasting of data
#################################
st.write("")
st.header("🎈 Prediction for Time-series")
dataframe = pd.merge(new_df, vendor_df, left_index=True, right_index=True)

dataframe.drop_duplicates()
dataframe.drop(columns=['dayofweek_y'], inplace=True)


df = dataframe['Transaction_Value'].groupby(dataframe['Date'].dt.to_period('D')).sum().to_frame()
df.Working_Date = df.to_timestamp()
df.reset_index(level=0, inplace=True)
df.rename(columns={'Date':'ds','Transaction_Value':'y'}, inplace=True)

df['ds'] = df['ds'].dt.to_timestamp('s').dt.strftime('%Y-%m-%d %H:%M:%S.000')

model = Prophet()
model.fit(df)


#future_dates = model.make_future_dataframe(periods=30)
#forecast = model.predict(future_dates)
#st.write("")
#st.subheader("🎈 Prediction for 30 Days")
#st.pyplot(model.plot(forecast))


# Prediction for 365 days 
future = model.make_future_dataframe(periods=365)

forecast = model.predict(future)

st.write("")

st.subheader("🎈 Prediction for 365 Days")
#fig1 = model.plot(forecast)
#st.pyplot(fig1)
st.write("")
#st.subheader("🎈 Interactive")
st.plotly_chart(plot_plotly(model, forecast))
st.write("")
st.subheader("🎈 Forecast Trends")
st.plotly_chart(plot_components_plotly(model, forecast))
st.write("")

#st.subheader("🎈 Seasonality, Holiday Effects, And Regressors")
#model = Prophet()
#model.add_country_holidays(country_name='IN')
#model.fit(df)
#forecast = model.predict(future)
#st.pyplot(model.plot_components(forecast))


st.sidebar.write("")
st.subheader("🎈 Thank you")