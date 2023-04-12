import time  
import numpy as np  
import pandas as pd  
import plotly.express as px  
import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter
import matplotlib
import webbrowser

@st.experimental_memo
def load_active_data():
    data = pd.read_excel('Track_Trace.xlsx')
    return data

# def load_data():
#     data = pd.read_pickle('Tradelane View.pkl')
#     return data

def load_data1():
    data = pd.read_excel('Track_Trace_data.xlsx')
    return data

# st.set_page_config(
#     page_title="Real-Time Data Science Dashboard",
#     page_icon="✅",
#     layout="wide",)

active = load_active_data()
#Profit = load_data()
Profit1 = load_data1()

active['Delayed percentage']=(active['Delayed percentage']).astype(int).astype(str)+"%"
active['On-Time percentage']=(active['On-Time percentage']).astype(int).astype(str)+ "%"
active['Reached before Estimated Time percentage']=(active['Reached before Estimated Time percentage']).astype(int).astype(str)+ "%"


Profit1['Delayed Percentage']=(Profit1['Delayed Percentage']).astype(int).astype(str)+"%"
Profit1['On-Time Percentage']=(Profit1['On-Time Percentage']).astype(int).astype(str)+ "%"
Profit1['Reached before Estimated Time percentage']=(Profit1['Reached before Estimated Time percentage']).astype(int).astype(str)+ "%"


body ="Track and Trace Analytics"
st.title(body, anchor=None)

body ="Transit Patterns across Trade Lanes"
st.title(body, anchor=None)
#active=active.style.hide_index()
#styler = active.style.hide_index()
#st.write(styler.head(n=5).to_html(), unsafe_allow_html=True)
#st.write(active.head(n=10).to_html(index=False), unsafe_allow_html=True)
st.write(active)

locations1= Profit1['TL_PORT_PAIR']
options1 = st.sidebar.multiselect('Select Trade Lane name',locations1)
outputdframe = pd.DataFrame(Profit1[Profit1.TL_PORT_PAIR.isin(options1)],columns=['TL_PORT_PAIR','Total Transactions','Delayed Percentage','On-Time Percentage',
'Reached before Estimated Time percentage'])

headers = {
    'selector': 'thead',
    'font-size':'17px',
    'text-align':'middle',
    'font-weight':'Bold',
    'props': 'background-color: green; color: Black;'}

#outputdframe.sort_values(['Percentage of Transactions falling below 50th decile'],ascending=False,inplace=True)
df2 = outputdframe.style.set_properties(**{'text-align': 'left'}).set_table_styles([headers])

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            <p style='text-align: middle;'</p>
            </style>
            """
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.table(df2)
#st.write(Profit1[Profit1.TL_PORT_PAIR.isin(options1)])

authorization_url = "Track_Trace.xlsx"
login = st.button('Data Reference',key="1")
if login:
  webbrowser.open(authorization_url)

# outputdframe = pd.DataFrame(active,columns=['TL_PORT_PAIR','Delayed','On-Time','Reached before Estimated Time','Total Transactions',
# 'Delayed Percentage','On-Time Percentage','Reached before Estimated Time Percentage'])

#st.sidebar.markdown("### select Trade Lane name")

# locations = Profit.TL_PORT_PAIR.unique().tolist()
# options = st.sidebar.multiselect('Select Trade Lane name',locations)

# if options:
#     fig = px.scatter(Profit[Profit.TL_PORT_PAIR.isin(options)],x="ETD_FILE_DATE",y="Difference_in_Duration",#size="Count of Transactions falling below 50th decile",
#                  color='Transit_Time_Status',
#                  hover_name="TL_PORT_PAIR",
#                  size_max=40)
#     fig.update_layout(height=850,width=1300,title_text='Transit-Time Patterns',xaxis_title="ETD FILE DATE",
#      yaxis_title="Difference in Duration",font=dict(size=19.5))
#     st.plotly_chart(fig)
# else:
#     fig = px.scatter(Profit,x="ETD_FILE_DATE",y="Difference_in_Duration",#size="Count of Transactions falling below 50th decile",
#                  color='Transit_Time_Status',
#                  hover_name="TL_PORT_PAIR",
#                  size_max=40)
#     fig.update_layout(height=850,width=1300,title_text='Transit-Time Patterns',xaxis_title="Percentage  of  Low  Profitability  Transactions",
#      yaxis_title="Total  no  of  Transactions",font=dict(size=19.5))
#     st.plotly_chart(fig)

# fig = px.histogram(Profit['Difference_in_Duration'])
# st.plotly_chart(fig)

# #fig=sns.distplot(Profit['Difference_in_Duration'])





