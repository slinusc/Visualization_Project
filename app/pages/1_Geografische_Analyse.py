import streamlit as st
import pandas as pd
import holoviews as hv
import sys
sys.path.insert(0, '../classes')
import relation_chord_chart as rcc
import geo_map as gm


@st.cache_data
def load_data():
    path = '../data/without_content.tsv.xz'
    df = pd.read_csv(path, sep='\t', compression='xz')
    df['countries'] = df['countries'].apply(eval)
    df['entities_header'] = df['entities_header'].apply(eval)
    df['people'] = df['people'].apply(eval)
    df['date'] = pd.to_datetime(df['date'])
    return df


df = load_data()

# layout streamlit app
col1, col2 = st.columns([1, 1])  # Widgets
col3= st.columns(1)  # Chord chart
full_width_col3 = st.columns(1)  # Geo map

# remove streamlit menu
st.markdown("""
                                    <style>
                                    #MainMenu {visibility: hidden;}
                                    footer {visibility: hidden;}
                                    </style>
                                    """, unsafe_allow_html=True)

# Filter data by date with streamlit date input
selected_date = col1.date_input("Wähle Datum",
                                value=pd.to_datetime('2022-02-24'),
                                min_value=pd.to_datetime('2022-01-01'),
                                max_value=pd.to_datetime('2022-12-31'))
selected_date = pd.to_datetime(selected_date)
filtered_df = df[df['date'] == selected_date]

# Filter data by category with streamlit dropdown
categories = df['article_category'].unique()
categories = ['Alle'] + list(categories)
category = col2.selectbox('Wähle Kategorie', categories)
if category != 'Alle':
    filtered_df = filtered_df[filtered_df['article_category'] == category]

# Create chord diagram
chord_chart = rcc.ChordCharts(filtered_df['countries']).country_chord_chart(threshold=5)
with col3[0]:
    st.bokeh_chart(hv.render(chord_chart, backend='bokeh'))

data_country_series = filtered_df['countries_en']
data_country_list = [eval(i) for i in data_country_series.dropna().tolist()]

world_map = gm.WorldMap(data_country_list)
world_map_chart = world_map.erstelle_weltkarte()
with full_width_col3[0]:
    st.plotly_chart(world_map_chart)

if __name__ == '__main__':
    import os

    print(os.getcwd())
