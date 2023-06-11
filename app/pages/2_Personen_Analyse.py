import streamlit as st
import pandas as pd
import holoviews as hv
import sys
import csv
sys.path.insert(0, r'C:\Users\aober\Documents\Data Science Studium\2 Semster\VDSS\semesterProjekt\visualization_project\app\classes')
import relation_chord_chart as rcc
import sent_sub_obj as sso
from topic_analysis import TopicAnalysis
from top_pers_coun import StackedBarPlot
import sentiment_plot as sp

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
st.header('Personen Analyse')
col1, col2, col3 = st.columns([1, 1, 1])  # Widgets
full_width_col1 = st.columns(1)
col4 = st.columns([2, 1])  # Chord chart & Sentiment / Objectivity
full_width_col2 = st.columns(1)
full_width_col3 = st.columns(1)  # Topic Analysis

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

# COUNTRY SELECTION (FILTER)
with col3:
    options = ['Alle'] + filtered_df['Personen'].explode().astype(str).unique().tolist()
    options = [i for i in options if i != 'nan']
    options = sorted(options)
    # create multiselect widget
    selected = st.multiselect('Wähle Persönlichkeit', options, default=['Alle'])

    if 'Alle' not in selected:
        filtered_df = filtered_df[filtered_df['Personen'].apply(lambda x: any(i in x for i in selected))]
    else:
        pass



# TOP 10 Personen
bar_chart = StackedBarPlot(filtered_df, filter='Personen')
fig = bar_chart.plot()
with full_width_col1[0]:
    st.subheader("Die häufigst vorkommenden Personen")
    st.plotly_chart(fig, config=config)


# CHORD RELATION DIAGRAM
chord_chart = rcc.ChordCharts(filtered_df['Länder']).country_chord_chart()
with col4[0]:
    st.subheader("Beziehung zwischen Ländern")
    st.button('ℹ️', help="")
    st.bokeh_chart(hv.render(chord_chart, backend='bokeh'))

# SENTIMENT PLOT
with col4[1]:
    st.set_option('deprecation.showPyplotGlobalUse', False)
    sentiment_plot = sp.SentimentObjectivityPlots(filtered_df['sentiment'], filtered_df['subjectivity'])
    st.subheader("Stimmung & Subjektivität")
    st.button('ℹ️', help="Die Stimmung und Subjektivität der Artikel wird in diesem Plot dargestellt.")
    st.plotly_chart(sentiment_plot.plot(), config=config)

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