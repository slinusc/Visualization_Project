from bokeh.io import show
from bokeh.plotting import figure
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.palettes import Category20c, Category10, Viridis3
from bokeh.transform import cumsum
from math import pi
import pandas as pd


class SentimentObjectivityPlots:
    def __init__(self, sentiment_list, subjectivity_list):
        self.sentiment_list = sentiment_list
        self.subjectivity_list = subjectivity_list
        self.sentiment_labels = ['negativ', 'neutral', 'positiv', 'sehr positiv']
        self.subjectivity_labels = ['objektiv','eher objektiv', 'eher subjektiv', 'subjektiv']

    def count_subjectivity(self):
        counts = [0, 0 ,0, 0]
        for subjectivity in self.subjectivity_list:
            if subjectivity < 0.1:
                counts[0] += 1
            elif subjectivity < 0.2:
                counts[1] += 1
            elif subjectivity < 0.4:
                counts[2] += 1
            else:
                counts[3] += 1
        return counts

    def count_sentiment(self):
        counts = [0, 0, 0, 0]
        for sentiment in self.sentiment_list:
            if sentiment < 0.0:
                counts[0] += 1
            elif sentiment < 0.25:
                counts[1] += 1
            elif sentiment < 0.5:
                counts[2] += 1
            else:
                counts[3] += 1
        return counts

    def plot(self):
        sentiment_counts = self.count_sentiment()
        subjectivity_counts = self.count_subjectivity()

        # Process the sentiment data
        sentiment_data = {
            'label': self.sentiment_labels,
            'counts': sentiment_counts,
            'angle': [count/sum(sentiment_counts)*2*pi for count in sentiment_counts],
            'color': Category20c[len(sentiment_counts)],
            'percent': [str(round(count/sum(sentiment_counts)*100, 2)) + "%" for count in sentiment_counts],
        }

        # Process the subjectivity data
        subjectivity_data = {
            'label': self.subjectivity_labels,
            'counts': subjectivity_counts,
            'angle': [count / sum(subjectivity_counts) * 2 * pi for count in subjectivity_counts],
            'color': Category20c[len(subjectivity_counts)],
            'percent': [str(round(count / sum(subjectivity_counts) * 100, 2)) + "%" for count in subjectivity_counts]
        }

        plots = []
        for data, title in zip([sentiment_data, subjectivity_data], ['Sentiment', 'Subjectivity']):
            source = ColumnDataSource(data=data)

            p = figure(tools="hover", tooltips="@percent: @label", x_range=(-.5, .5))

            p.annular_wedge(x=0, y=1, inner_radius=0.2, outer_radius=0.4,
                            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
                            line_color="white", fill_color='color', source=source
                            )

            p.axis.axis_label=None
            p.axis.visible=False
            p.grid.grid_line_color = None
            p.border_fill_color = None
            p.outline_line_color = None

            plots.append(p)

        grid = gridplot(plots, ncols=1, plot_width=250, plot_height=250, toolbar_location=None)

        # Show the plot
        return grid


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
    plotter.plot()
