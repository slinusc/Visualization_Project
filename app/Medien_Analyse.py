import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from classes.linechart_categories import LinechartCategories
from classes.line_chart_medium import NewspaperCategoryPlot

st.set_page_config(layout="wide")
def main():
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
    full_width_col0 = st.columns(1)  # Line charts
    full_width_col1 = st.columns(1)  # Line chart
    full_width_col2 = st.columns(1)  # Dataframe

    # remove streamlit menu
    st.markdown("""
                            <style>
                            #MainMenu {visibility: hidden;}
                            footer {visibility: hidden;}
                            </style>
                            """, unsafe_allow_html=True)

    # Filter data by date with streamlit date input
    with col1:
        start_date, end_date = st.date_input(
            "Wählen Sie einen Datumsbereich",
            [pd.to_datetime('2022-01-01'), pd.to_datetime('2022-01-31')],
            min_value=pd.to_datetime('2022-01-01'),
            max_value=pd.to_datetime('2022-12-31')
        )
        st.button('Info Datumsbereich', help='Wählen Sie den Start- und Enddatumsbereich aus, für den Sie Daten '
                                             'anzeigen möchten. In dieser Version der App kann jeder beliebige '
                                             'Zeitraum im Jahr 2022 ausgewählt werden. Es kann auch jeder Tag einzeln '
                                             'analysiert werden.')
        start_date = pd.Timestamp(start_date)
        end_date = pd.Timestamp(end_date)
        filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    # Filter data by category with streamlit multiselect
    with col2:
        categories = df['article_category'].unique()
        categories_options = ['Alle'] + list(categories)
        selected_categories = st.multiselect('Wähle Kategorie', categories_options, default=['Alle'])
        st.button('Info Kategorien', help='Wählen Sie die Kategorien aus, die Sie im Diagramm anzeigen möchten. '
                                          'Die Kategorien wurden von den Autoren definiert und zusammengestellt. ')
        if 'Alle' in selected_categories:
            # all categories are selected, no filtering needed
            pass
        else:
            filtered_df = filtered_df[filtered_df['article_category'].isin(selected_categories)]

    # Filter data by medium_name with streamlit multiselect
    with col3:
        newspapers = df['medium_name'].unique()
        newspapers_options = ['Alle'] + list(newspapers)
        selected_newspapers = st.multiselect('Wähle Zeitung', newspapers_options, default=['Alle'])
        st.button('Info Zeitungen', help='Wählen Sie die Zeitungen aus, deren Daten Sie im Diagramm anzeigen möchten. '
                                         'In dieser Version stehen acht Zeitungen zur Verfügung.')

        if 'Alle' in selected_newspapers:
            # all newspapers are selected
            selected_newspapers = newspapers
        else:
            filtered_df = filtered_df[filtered_df['medium_name'].isin(selected_newspapers)]

    # Check if start and end date are the same
    if start_date != end_date:
        # Create linechart plot
        linechart_generator = LinechartCategories()
        linechart_plot = linechart_generator.linechart_categories(filtered_df)
        with full_width_col0[0]:
            st.subheader('Anzahl Artikel nach Kategorien')
            st.button('Info', help='Es werden die Anzahl der Artikel pro Kategorie angezeigt.')
            st.plotly_chart(linechart_plot)

        # Create line chart medium
        line_chart = NewspaperCategoryPlot(filtered_df, selected_categories)
        line_medium = line_chart.plot_newspaper_category()
        with full_width_col1[0]:
            st.subheader('Anzahl Artikel nach Zeitung')
            st.button('Info', help='Es werden die Anzahl der Artikel pro Zeitung angezeigt.')
            st.plotly_chart(line_medium)
    else:
        fig = go.Figure()
        for newspaper in selected_newspapers:
            newspaper_df = filtered_df[filtered_df['medium_name'] == newspaper]
            category_frequencies = newspaper_df['article_category'].value_counts()
            fig.add_trace(go.Bar(
                x=category_frequencies.index,
                y=category_frequencies.values,
                name=newspaper
            ))

        fig.update_layout(xaxis_title='Kategorie',
                          yaxis_title='Häufigkeit',
                          barmode='stack',
                          width=1000, height=500)
        with full_width_col1[0]:
            st.subheader('Häufigkeiten nach Kategorien')
            st.plotly_chart(fig)

    # Create dataframe
    with full_width_col2[0]:
        filtered_df.columns = ['Medium', 'Headline', 'Datum', 'Länder', 'sentiment', 'subjectivity',
                      'entities_header', 'Kategorie', 'countries_en', 'Personen']
        filtered_df['Datum'] = filtered_df['Datum'].dt.strftime('%d.%m.%Y')
        st.subheader('Artikeltabelle')
        st.button('Info Artikeltabelle', help='Die Tabelle zeigt die Artikel an, nach denen die Filter gesetzt wurden.')
        st.dataframe((filtered_df.loc[:, ['Medium', 'Headline','Kategorie',  'Datum']]))

if __name__ == "__main__":
    main()
