import plotly.express as px
import pandas as pd

class StackedBarPlot:

    def __init__(self, df, filter):
        self.df = df
        self.filter = filter

    def preprocess(self):
        column_name = 'Länder' if self.filter == 'country' else 'Personen'
        self.df = self.df.explode(column_name)
        if column_name == 'Länder':
            top_10 = self.df[column_name].value_counts().index[:10]
        else:
            top_10 = self.df[column_name].value_counts().index[:20]

        self.df = self.df[self.df[column_name].isin(top_10)]
        self.df = self.df.groupby([self.df[column_name], 'Kategorie']).size().reset_index(name='counts')
        total_counts = self.df.groupby(column_name)['counts'].sum().reset_index(name='total_counts')
        self.df = pd.merge(self.df, total_counts, on=column_name)
        self.df.sort_values(['total_counts', 'Kategorie'], ascending=[False, True], inplace=True)

    def plot(self):
        self.preprocess()
        column_name = 'Länder' if self.filter == 'country' else 'Personen'
        sorted_categories = self.df[column_name].unique().tolist()
        if self.filter == 'country':
            fig = px.bar(self.df, y=column_name, x='counts', color='Kategorie',
                         labels={column_name: '', 'Kategorie': 'Kategorie', 'counts': 'Anzahl'},
                         height=600,
                         width=400,
                         category_orders={column_name: sorted_categories})
            fig.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                x=0,
                borderwidth=10,
                xanchor="left"))
        else:
            fig = px.bar(self.df, x=column_name, y='counts', color='Kategorie',
                         labels={column_name: 'Personen', 'Kategorie': 'Kategorie', 'counts': 'Anzahl'},
                         height=600,
                         width=1100,
                         category_orders={column_name: sorted_categories})
        return fig



