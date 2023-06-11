from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.colors

class SentimentObjectivityPlots:
    def __init__(self, sentiment_list, subjectivity_list):
        self.sentiment_list = sentiment_list
        self.subjectivity_list = subjectivity_list
        self.sentiment_labels = ['negativ', 'sehr positiv', 'positiv', 'neutral']
        self.subjectivity_labels = ['subjektiv', 'objektiv', 'eher objektiv', 'eher subjektiv']
        self.sentiment_colors = ['red','#0068c9', '#83c9ff', '#ffabab']
        self.subjectivity_colors = ['red','#0068c9', '#83c9ff', '#ffabab']

    def count_subjectivity(self):
        counts = [0, 0, 0, 0]
        for subjectivity in self.subjectivity_list:
            if subjectivity < 0.1:
                counts[1] += 1
            elif subjectivity < 0.2:
                counts[2] += 1
            elif subjectivity < 0.4:
                counts[3] += 1
            else:
                counts[0] += 1
        return counts

    def count_sentiment(self):
        counts = [0, 0, 0, 0]
        for sentiment in self.sentiment_list:
            if sentiment < 0.0:
                counts[0] += 1
            elif sentiment < 0.25:
                counts[3] += 1
            elif sentiment < 0.5:
                counts[2] += 1
            else:
                counts[1] += 1
        return counts

    def plot(self):
        sentiment_counts = self.count_sentiment()
        subjectivity_counts = self.count_subjectivity()

        sentiment_median = np.median(self.sentiment_list)
        objectivity_median = 1 - np.median(self.subjectivity_list)

        fig = make_subplots(rows=2, cols=1,
                            specs=[[{'type': 'domain'}], [{'type': 'domain'}]], vertical_spacing=0.05, horizontal_spacing=0.05)

        fig.add_trace(go.Pie(labels=self.sentiment_labels,
                             values=sentiment_counts,
                             name='Sentiment',
                             hole=.5,
                             marker=dict(colors=self.sentiment_colors),
                             showlegend=False,
                             sort=False,
                             ),
                      row=1, col=1)

        fig.add_trace(go.Pie(labels=self.subjectivity_labels,
                             values=subjectivity_counts,
                             name='Subjectivity',
                             hole=.5,
                             marker=dict(colors=self.subjectivity_colors),
                             showlegend=False,
                             sort=False,
                             ),
                      row=2, col=1)

        # Add annotations in the center of the donuts
        fig.add_annotation(text='Stimmung: <br> {:.2f}'.format(sentiment_median),
                           xref='paper', yref='paper',
                           x=0.5, y=.8, showarrow=False)
        fig.add_annotation(text='Objektivität: <br> {:.2f}'.format(objectivity_median),
                           xref='paper', yref='paper',
                           x=0.5, y=.19, showarrow=False)

        fig.update_layout(
            height=450,
            width=450,
            margin=dict(l=0, r=0, t=0, b=15),
            template='plotly_white',
            # Konfiguration für das Entfernen des Plotly-Logos
            showlegend=False
        )

        return fig


if '__main__' == __name__:
    def load_data():
        path = '../processed_data/without_content.tsv.xz'
        df = pd.read_csv(path, sep='\t', compression='xz')
        df['countries'] = df['countries'].apply(eval)
        df['entities_header'] = df['entities_header'].apply(eval)
        df['people'] = df['people'].apply(eval)
        df['date'] = pd.to_datetime(df['date'])
        return df

    df = load_data()
    sentiments = df['sentiment']
    subjectivities = df['subjectivity']
    plotter = SentimentObjectivityPlots(sentiments, subjectivities)
    fig = plotter.plot()
