import streamlit as st
st.header('dash board')
import pandas as pd
data=pd.read_csv('/workspaces/streamlit.dashboard/mentornow/timesData.csv')
with st.expander('show data'):
    st.write(data)
import plotly.express as px
fig=px.line(data.iloc[:100],x='world_rank',y='citations')
st.plotly_chart(fig)