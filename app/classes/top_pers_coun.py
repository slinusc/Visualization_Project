import plotly.express as px

class StackedBarPlot:

    def __init__(self, df):
        self.df = df

    def preprocess(self):
        self.df = self.df.explode(self.df['Länder'])
        top_countries = self.df[self.df['Länder']].value_counts().index[:10]
        self.df = self.df[self.df[self.df['Länder']].isin(top_countries)]
        self.df = self.df.groupby([self.df['Länder'], self.df['Länder']]).size().reset_index(name='counts')

    def plot(self):
        self.preprocess()
        fig = px.bar(self.df, x=self.df['Länder'], y='counts', color=self.df['Kategorie'],
                     labels={self.df['Länder']: 'Country', self.df['Kategorie']: 'Category', 'counts': 'Counts'},
                     title='Top 10 Länder by Category',
                     height=400)
        return fig

import unittest
import pandas as pd

class TestStackedBarPlot(unittest.TestCase):

    def setUp(self):
        self.data = {'Länder': [['USA', 'Canada'], ['UK', 'USA'], ['Canada', 'UK', 'USA'], ['USA'], ['Canada'], ['UK']],
                     'Kategorie': ['A', 'B', 'A', 'B', 'A', 'B']}
        self.df = pd.DataFrame(self.data)
        self.plotter = StackedBarPlot(self.df)

    def test_preprocess(self):
        self.plotter.preprocess()
        # Check if preprocess method works correctly
        self.assertEqual(self.plotter.df['Länder'].nunique(), 3)
        self.assertEqual(self.plotter.df['Kategorie'].nunique(), 2)
        self.assertTrue(set(self.plotter.df['Länder'].unique()).issubset(['USA', 'UK', 'Canada']))
        self.assertTrue(set(self.plotter.df['Kategorie'].unique()).issubset(['A', 'B']))

if __name__ == '__main__':
    unittest.main()
