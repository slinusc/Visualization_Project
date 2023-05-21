import itertools
import pandas as pd
import holoviews as hv
from holoviews import opts, dim, Dataset


class ChordCharts:

    def __init__(self, data):
        self.data = data.tolist()
        self.edges_list = []

    def threshold_filter(self, threshold):
        for connection in self.data:
            for pair in itertools.combinations(connection, 2):
                self.edges_list.append(pair)
        edges_df = pd.DataFrame(self.edges_list, columns=['source', 'target'])
        edges_count = edges_df.groupby('source').count()
        edges_count.columns = ['count']
        filtered_countries = edges_count[edges_count['count'] >= threshold].index
        filtered_edges_df = edges_df[
            edges_df['source'].isin(filtered_countries) & edges_df['target'].isin(filtered_countries)]
        edges_ds = Dataset(filtered_edges_df, ['source', 'target'])
        return edges_ds

    def country_chord_chart(self, threshold=3):
        hv.extension('bokeh')
        chord = hv.Chord(self.threshold_filter(threshold)).select(value=(1, None))
        return chord.opts(
            opts.Chord(
                cmap='Category20',
                edge_cmap='Category20',
                edge_color=dim('source').str(),
                labels='index',
                node_color=dim('index').str(),
                width=650,
                height=650,
                tools=['tap']
            )
        )