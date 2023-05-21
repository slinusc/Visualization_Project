import pandas as pd
import plotly
import plotly.graph_objects as go


class SentimentPlot:
    def __init__(self, sentiment_list):
        self.sentiment_list = sentiment_list
        self.balken_labels = ['--', '-', '+', '++']
        self.balken_breiten = [0, 0, 0, 0]
        self.balken_farben = ['goldenrod', 'gold', 'limegreen', 'green']
        self.fig = go.Figure()

    def count_sentiment(self):
        for sentiment in self.sentiment_list:
            if sentiment < -0.5:
                self.balken_breiten[0] += 1
            elif sentiment < 0:
                self.balken_breiten[1] += 1
            elif sentiment < 0.5:
                self.balken_breiten[2] += 1
            else:
                self.balken_breiten[3] += 1

    def add_bars(self):
        x_start = 0
        for i in range(len(self.balken_labels)):
            x_end = x_start + self.balken_breiten[i]
            self.fig.add_shape(type='rect',
                               x0=x_start, y0=0,
                               x1=x_end, y1=1,
                               fillcolor=self.balken_farben[i],
                               line_width=0)
            x_center = (x_start + x_end) / 2
            y_center = 0.5
            self.fig.add_annotation(
                x=x_center, y=y_center,
                text=self.balken_labels[i],
                showarrow=False,
                font=dict(color='white', size=14),
                xanchor='center', yanchor='middle'
            )
            x_start = x_end

    def create_plot(self):
        self.count_sentiment()
        self.add_bars()
        self.fig.update_layout(
            title='Stimmung',
            xaxis=dict(
                range=[0, len(self.sentiment_list)],
                showticklabels=False
            ),
            yaxis=dict(
                range=[0, 1],
                showticklabels=False
            ),
            height=300
        )
        return self.fig



class SubjectivityPlot:
    def __init__(self, subjectivity_list):
        self.subjectivity_list = subjectivity_list
        self.balken_labels = ['OBJ', 'SUB']
        self.balken_breiten = [0, 0]
        self.balken_farben = ['lightseagreen', 'mediumblue']
        self.fig = go.Figure()

    def count_subjectivity(self):
        for subjectivity in self.subjectivity_list:
            if subjectivity < 0.5:
                self.balken_breiten[0] += 1
            else:
                self.balken_breiten[1] += 1

    def add_bars(self):
        x_start = 0
        for i in range(len(self.balken_labels)):
            x_end = x_start + self.balken_breiten[i]
            self.fig.add_shape(type='rect',
                               x0=x_start, y0=0,
                               x1=x_end, y1=1,
                               fillcolor=self.balken_farben[i],
                               line_width=0)
            x_center = (x_start + x_end) / 2
            y_center = 0.5
            self.fig.add_annotation(
                x=x_center, y=y_center,
                text=self.balken_labels[i],
                showarrow=False,
                font=dict(color='white', size=14),
                xanchor='center', yanchor='middle'
            )
            x_start = x_end

    def create_plot(self):
        self.count_subjectivity()
        self.add_bars()
        self.fig.update_layout(
            title='Subjektivität',
            xaxis=dict(
                range=[0, len(self.subjectivity_list)],
                showticklabels=False
            ),
            yaxis=dict(
                range=[0, 1],
                showticklabels=False
            ),
            height=300
        )
        return self.fig