import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime
import plotly.graph_objs as go
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure



# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv('../data/processed_data_final.tsv.xz', sep='\t', compression='xz')
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

values = st.slider(
    'Select a range of dates',
    min_value=datetime(2022, 1, 1), format="YYYY/MM/DD", max_value=datetime(2022, 12, 31), value =(datetime(2022, 7, 1), datetime(2022, 9, 1)))


filtered_df = df.loc[(df['date'] >= values[0]) & (df['date'] <= values[1]), ['article_category', 'date']]


##plot 2
df_grouped = filtered_df.groupby(['date', 'article_category']).size().reset_index(name='count')

# Create a colored line chart with Plotly Express
fig = px.line(df_grouped, x='date', y='count', color='article_category')

fig.update_layout(title='Line Chart of Medium Names', xaxis_title='Date', yaxis_title='Count')


st.plotly_chart(fig)