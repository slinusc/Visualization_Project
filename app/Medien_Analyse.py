import streamlit as st
import pandas as pd
from classes.linechart_categories import LinechartCategories
from classes.line_chart_medium import NewspaperCategoryPlot


def main():
    st.set_page_config(layout="wide")
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
    col1, col2, col3 = st.columns([1, 1, 1])  # Widgets
    full_width_col1 = st.columns(1)  # Line chart
    full_width_col0 = st.columns(1)  # Line charts

    # remove streamlit menu
    st.markdown("""
                            <style>
                            #MainMenu {visibility: hidden;}
                            footer {visibility: hidden;}
                            </style>
                            """, unsafe_allow_html=True)

    # Filter data by date with streamlit date input
    start_date, end_date = col1.date_input(
        "Wählen Sie einen Datumsbereich",
        [pd.to_datetime('2022-01-01'), pd.to_datetime('2022-01-31')],
        min_value=pd.to_datetime('2022-01-01'),
        max_value=pd.to_datetime('2022-12-31'))

    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date)

    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    # Filter data by category with streamlit dropdown
    categories = df['article_category'].unique()
    categories = ['Alle'] + list(categories)
    category = col2.selectbox('Wähle Kategorie', categories)
    if category != 'Alle':
        filtered_df = filtered_df[filtered_df['article_category'] == category]

    # Filter data by medium_name with streamlit dropdown
    newspapers = df['medium_name'].unique()
    newspapers = ['Alle'] + list(newspapers)
    selected_newspaper = col3.selectbox('Wähle Zeitung', newspapers)
    if selected_newspaper != 'Alle':
        filtered_df = filtered_df[filtered_df['medium_name'] == selected_newspaper]

    # Create linechart plot
    linechart_generator = LinechartCategories()
    linechart_plot = linechart_generator.linechart_categories(filtered_df)
    with full_width_col1[0]:
        st.plotly_chart(linechart_plot)

    # Create line chart medium
    line_chart = NewspaperCategoryPlot(filtered_df, category)
    line_medium = line_chart.plot_newspaper_category()
    with full_width_col0[0]:
        st.plotly_chart(line_medium)



if __name__ == "__main__":
    main()
