import plotly.express as px
import pandas as pd

class TopicAnalysis:

    def __init__(self, df):
        self.df = df

    def preprocess(self):
        column_name = 'Entitäten Header'
        self.df = self.df.explode(column_name)
        top_n = self.df[column_name].value_counts().index[:20]

        self.df = self.df[self.df[column_name].isin(top_n)]
        self.df = self.df.groupby([self.df[column_name], 'Medium']).size().reset_index(name='counts')
        total_counts = self.df.groupby(column_name)['counts'].sum().reset_index(name='total_counts')
        self.df = pd.merge(self.df, total_counts, on=column_name)
        self.df.sort_values(['total_counts', 'Medium'], ascending=[False, True], inplace=True)

    def plot(self):
        self.preprocess()
        column_name = 'Entitäten Header'
        sorted_categories = self.df[column_name].unique().tolist()



        fig = px.bar(self.df, x=column_name, y='counts', color='Medium',
                     labels={column_name: 'Topic', 'Medium': 'Medium', 'counts': 'Anzahl'},
                     height=600,
                     width=1100,
                     category_orders={column_name: sorted_categories})
        return fig



