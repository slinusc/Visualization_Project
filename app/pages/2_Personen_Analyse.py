import streamlit as st
import pandas as pd
import holoviews as hv
import sys
sys.path.insert(0, r'C:\Users\aober\Documents\Data Science Studium\2 Semster\VDSS\semesterProjekt\visualization_project\app\classes')
import relation_chord_chart as rcc
import sent_sub_obj as sso
from topic_analysis import TopicAnalysis
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

# layout streamlit app
col1, col2 = st.columns([1, 1])  # Widgets
full_width_col1 = st.columns(1)
full_width_col2 = st.columns(1)
full_width_col3 = st.columns(1)  # Topic Analysis
col4 = st.columns([1, 1])  # Chord chart & Sentiment / Objectivity

# CONFIG FOR ALL PLOTS
config = dict({'displayModeBar': False})

# remove streamlit menu
st.markdown("""
                                <style>
                                #MainMenu {visibility: hidden;}
                                footer {visibility: hidden;}
                                .st-dd {color: white; background-color: #1f77b4;}
                                </style>
                                """, unsafe_allow_html=True)

# DATE SELECTION
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


# TOP 10 Personen
bar_chart = StackedBarPlot(filtered_df, filter='Personen')
fig = bar_chart.plot()
with full_width_col1[0]:
    st.subheader("Die häufigst genannten Personen")
    st.plotly_chart(fig)


# CHORD DIAGRAM
chord_chart_people = rcc.ChordCharts(filtered_df['Personen']).country_chord_chart()
with col4[0]:
    st.bokeh_chart(hv.render(chord_chart_people, backend='bokeh', config=dict({'toolbar.logo': None})))


# SENTIMENT PLOT
sentiment_plot = sso.SentimentPlot(filtered_df['sentiment'])
sentiment_plot.create_plot()
with col4[1]:
    st.subheader('Stimmung')
    st.plotly_chart(sentiment_plot.fig, config=config)

# SUBJECTIVITY PLOT
subjectivity_plot = sso.SubjectivityPlot(filtered_df['subjectivity'])
subjectivity_plot.create_plot()
with col4[1]:
    st.header("Subjektivität")
    st.button('ℹ️', help='Das subjektivitäts Balkendiagramm visualisiert wie objektiv die Artikel geschrieben sind, oder beziehungsweise subjektiv.')
    st.plotly_chart(subjectivity_plot.fig, config=config)

# TOPIC ANALYSIS
with full_width_col2[0]:
    st.subheader('Themen Analyse')
    st.button('ℹ️', help='Die Themen Analyse zeigt die am häufigsten vorkommenden Wörter '
                         'in den Artikeln an.')
    topic_analysis = TopicAnalysis()
    st.plotly_chart(topic_analysis.plot_most_common_words(filtered_df['Entitäten Header'], 20), config=config)

# DATA TABLE
with full_width_col3[0]:
    filtered_df['Datum'] = filtered_df['Datum'].dt.strftime('%d.%m.%Y')
    st.subheader('Artikeltabelle')
    st.button('ℹ️', help='Die Tabelle zeigt die Artikel an, nach denen die Filter gesetzt wurden.')
    st.dataframe(filtered_df.loc[:, ['Medium', 'Headline', 'Kategorie', 'Datum']], width=1100)