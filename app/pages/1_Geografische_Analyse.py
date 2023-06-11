import streamlit as st
import pandas as pd
import holoviews as hv
import sys
import csv

sys.path.insert(0, 'C:/Users/linus/OneDrive/BSc_Data_Science/Semester_2/Data_Visualisation/'
                   'visualization_project/app/classes')
import relation_chord_chart as rcc
import geo_map as gm
from topic_analysis import TopicAnalysis
import sentiment_plot as sp
from top_pers_coun import StackedBarPlot


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
df.columns = ['Medium', 'Headline', 'Datum', 'Länder', 'sentiment', 'subjectivity',
                           'Entitäten Header', 'Kategorie', 'Länder (englisch)', 'Personen']

# LAYOUT STREAMLIT APP
st.header('Geografische Analyse')
st.button('ℹ️', help="Mit den Filteroptionen können Sie die angezeigten Daten nach spezifischen "
                     "Kriterien einschränken. Die verfügbaren Filteroptionen sind: \n"
                     "1. Datum: Mit dieser Option können Sie ein beliebiges Datum auswählen."
                     "möglich, Daten für jeden beliebigen Tag im Jahr 2022 zu analysieren. \n\n"
                     "2. Kategorie: Hier können Sie auswählen, welche Artikelkategorien in den Daten enthalten "
                     "sein sollen. \n"
                     "3. Länder: Mit dieser Option können Sie auswählen, nach welchen Ländern die Daten "
                     "gefiltert gefiltert werden sollen.\n")

col1, col2, col3 = st.columns([1, 1, 1])  # Widgets
left_col, right_col = st.columns([2, 1])  # Geo map
col4 = st.columns([2, 1])  # Chord chart & Sentiment / Objectivity
full_width_col2 = st.columns(1)  # Topic Analysis
full_width_col3 = st.columns(1)  # Dataframe

# HIDE STREAMLIT MENU
st.markdown("""
                                    <style>
                                    #MainMenu {visibility: hidden;}
                                    footer {visibility: hidden;}
                                    .st-dd {color: white; background-color: #1f77b4;}
                                    </style>
                                    """, unsafe_allow_html=True)

# CONFIG FOR ALL PLOTS
config = dict({'displayModeBar': False})

# DATE SELECTION (FILTER)
selected_date = col1.date_input("Wähle Datum",
                                value=pd.to_datetime('2022-02-24'),
                                min_value=pd.to_datetime('2022-01-01'),
                                max_value=pd.to_datetime('2022-12-31'))
selected_date = pd.to_datetime(selected_date)
filtered_df = df[df['Datum'] == selected_date]

# CATEGORY SELECTION (FILTER)
with col2:
    categories = df['Kategorie'].unique()
    categories_options = ['Alle'] + list(categories)
    selected_categories = st.multiselect('Wähle Kategorie', categories_options, default=['Alle'])
    if 'Alle' not in selected_categories:
        filtered_df = filtered_df[filtered_df['Kategorie'].isin(selected_categories)]
    else:
        pass

# COUNTRY SELECTION (FILTER)
with col3:
    options = ['Alle'] + filtered_df['Länder'].explode().astype(str).unique().tolist()
    options = [i for i in options if i != 'nan']
    options = sorted(options)
    # create multiselect widget
    selected = st.multiselect('Wähle Land', options , default=['Alle'])

    if 'Alle' not in selected:
        filtered_df = filtered_df[filtered_df['Länder'].apply(lambda x: any(i in x for i in selected))]
    else:
        pass

# WORLDMAP

with left_col:
    data_country_series = filtered_df['Länder (englisch)']
    data_country_list = [eval(i) for i in data_country_series.dropna().tolist()]

    world_map = gm.WorldMap(data_country_list)
    world_map_chart = world_map.erstelle_weltkarte()
    #st.subheader("Ländernennung")
    #st.button('ℹ️', help="Die Weltkarte stellt diejenigen Länder dar, die in Artikeln genannt wurden. Bei Filterung "
    #                     "nach einem spezifischen Land, werden ausserdem diejenigen Länder angezeigt, die zusammen mit"
    #                     "dem gesuchten Land genannt wurden. \n")
    st.plotly_chart(world_map_chart, config={'scrollZoom': False, 'displayModeBar': False}, use_container_width=True)

# TOP 10LÄNDER

with right_col:
    bar_chart = StackedBarPlot(filtered_df, filter='country')
    fig = bar_chart.plot()
    st.subheader("")
    st.plotly_chart(fig, config=config)


# CHORD RELATION DIAGRAM
chord_chart = rcc.ChordCharts(filtered_df['Länder']).country_chord_chart()
with col4[0]:
    st.subheader("Beziehung zwischen Ländern")
    st.bokeh_chart(hv.render(chord_chart, backend='bokeh'))

# SENTIMENT PLOT
with col4[1]:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    sentiment_plot = sp.SentimentObjectivityPlots(filtered_df['sentiment'], filtered_df['subjectivity'])
    st.subheader("Stimmung & Subjektivität")
    st.button('ℹ️', help="")
    st.plotly_chart(sentiment_plot.plot())

# TOPIC ANALYSIS
with full_width_col2[0]:
    st.subheader('Themen Analyse')
    st.button('ℹ️', help='Die Themen Analyse zeigt die am häufigsten vorkommenden Wörter '
                         'in den Artikeln an.')
    topic_analysis = TopicAnalysis()
    st.plotly_chart(topic_analysis.plot_most_common_words(filtered_df['Entitäten Header'], 20),config=config)

# DATA TABLE
with full_width_col3[0]:
    filtered_df['Datum'] = filtered_df['Datum'].dt.strftime('%d.%m.%Y')
    st.subheader('Artikeltabelle')
    st.button('ℹ️', help='Die Tabelle zeigt die Artikel an, nach denen die Filter gesetzt wurden.')
    st.dataframe(filtered_df.loc[:, ['Medium', 'Headline', 'Kategorie', 'Datum']], width=1100)

if __name__ == '__main__':
    pass
