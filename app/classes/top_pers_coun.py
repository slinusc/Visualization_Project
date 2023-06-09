import plotly.express as px
import pandas as pd
import unittest

class StackedBarPlot:

    def __init__(self, df, filter):
        self.df = df
        self.filter = filter

    def preprocess(self):
        column_name = 'Länder' if self.filter == 'country' else 'Personen'
        self.df = self.df.explode(column_name)
        top_10 = self.df[column_name].value_counts().index[:10]
        self.df = self.df[self.df[column_name].isin(top_10)]
        self.df = self.df.groupby([self.df[column_name], 'Kategorie']).size().reset_index(name='counts')

        # Calculate total counts for each category
        total_counts = self.df.groupby(column_name)['counts'].sum().reset_index(name='total_counts')

        # Merge total_counts with self.df
        self.df = pd.merge(self.df, total_counts, on=column_name)

        # Sort by total_counts in descending order
        self.df.sort_values('total_counts', ascending=False, inplace=True)

    def plot(self):
        self.preprocess()
        column_name = 'Länder' if self.filter == 'country' else 'Personen'
        sorted_categories = self.df[column_name].unique().tolist()
        if self.filter == 'country':
            fig = px.bar(self.df, y=column_name, x='counts', color='Kategorie',
                         labels={column_name: 'Country', 'Kategorie': 'Category', 'counts': 'Counts'},
                         height=600,
                         width=400,
                         category_orders={column_name: sorted_categories})
        else:
            fig = px.bar(self.df, x=column_name, y='counts', color='Kategorie',
                         labels={column_name: 'Person', 'Kategorie': 'Category', 'counts': 'Counts'},
                         height=600,
                         category_orders={column_name: sorted_categories})
        return fig



