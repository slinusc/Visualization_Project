import streamlit as st
import pandas as pd
import holoviews as hv
from visualization_classes import relation_chord_chart as rcc
from visualization_classes import geo_map as gm
from visualization_classes.sent_sub_obj import SentimentPlot, SubjectivityPlot


def main():

    # layout streamlit app
    st.set_page_config(layout="wide")
    col1, col2 = st.columns([1, 1])

    # remove streamlit menu
    st.markdown("""
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """, unsafe_allow_html=True)
    # load data

    def load_data():
        path = '../data/without_content.tsv.xz'
        df = pd.read_csv(path, sep='\t', compression='xz')
        df['countries'] = df['countries'].apply(eval)
        df['date'] = pd.to_datetime(df['date'])
        return df
    df = load_data()

    # Filter data by date with streamlit date input
    selected_date = col1.date_input("Wähle Datum",
                                  value=pd.to_datetime('2022-01-01'),
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
    with col1:
        st.bokeh_chart(hv.render(chord_chart, backend='bokeh'))


    # Create chord diagram
    """
    chord_chart_persons = rcc.ChordCharts(filtered_df['entities_header']).country_chord_chart(threshold=5)
    with col2:
        st.bokeh_chart(hv.render(chord_chart_persons, backend='bokeh'))
    """
    df_grouped = filtered_df.groupby(['date', 'article_category']).size().reset_index(name='count')

    # Create a colored line chart with Plotly Express
    fig = px.line(df_grouped, x='date', y='count', color='article_category')

    fig.update_layout(title='Line Chart of Medium Names', xaxis_title='Date', yaxis_title='Count')

    st.plotly_chart(fig)


if __name__ == "__main__":
    main()
