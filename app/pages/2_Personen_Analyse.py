import streamlit as st
import pandas as pd
import holoviews as hv
import sys
sys.path.insert(0, 'C:/Users/linus/OneDrive/BSc_Data_Science/Semester_2/Data_Visualisation/visualization_project/app'
                   '/classes')
import relation_chord_chart as rcc
import sent_sub_obj as sso
import wordclound as wc

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
col4 = st.columns([1, 1])  # Chord chart
full_width_col2 = st.columns(1)  # Wordcloud
col5, col6 = st.columns([1, 1])  # Sentiment / Subjectivity
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
chord_chart_people = rcc.ChordCharts(filtered_df['people']).country_chord_chart(threshold=1)
with col4[0]:
    st.bokeh_chart(hv.render(chord_chart_people, backend='bokeh'))

# Create word cloud

entities_header = filtered_df['entities_header'].dropna().tolist()
word_cloud = wc.theWordCloud(entities_header)
generated_wordcloud = word_cloud.generate_wordcloud()
with full_width_col2[0]:
    st.pyplot(word_cloud.display_wordcloud(generated_wordcloud))

# Create sentiment plot
sentiment_plot = sso.SentimentPlot(filtered_df['sentiment'])
sentiment_plot.create_plot()
with col5:
    st.plotly_chart(sentiment_plot.fig)

# Create subjectivity plot
subjectivity_plot = sso.SubjectivityPlot(filtered_df['subjectivity'])
subjectivity_plot.create_plot()
with col6:
    st.plotly_chart(subjectivity_plot.fig)
