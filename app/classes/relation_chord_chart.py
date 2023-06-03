import itertools
import pandas as pd
import holoviews as hv
from holoviews import opts, dim, Dataset

class ChordCharts:

    def __init__(self, data):
        self.data = data.tolist()
        self.edges_list = []

    def create_edges(self):
        for connection in self.data:
            for pair in itertools.combinations(connection, 2):
                self.edges_list.append(pair)
        edges_df = pd.DataFrame(self.edges_list, columns=['source', 'target'])
        edges_ds = Dataset(edges_df, ['source', 'target'])
        return edges_ds

    def country_chord_chart(self):
        hv.extension('bokeh')
        chord = hv.Chord(self.create_edges()).select(value=(1, None))
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

if __name__ == '__main__':
    data = [['Ukraine, Deutschland'], ['Deutschland', 'USA'], ['USA', 'Deutschland'], ['Ukraine', 'USA']]
    test = ChordCharts(data)
    test.country_chord_chart()
