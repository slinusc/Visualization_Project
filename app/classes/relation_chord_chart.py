import itertools
import pandas as pd
import holoviews as hv
from holoviews import opts, dim

class ChordCharts:

    def __init__(self, data):
        self.data = data
        self.edges_list = []

    def create_edges(self):
        for connection in self.data:
            for pair in itertools.combinations(connection, 2):
                self.edges_list.append(pair)
        edges_df = pd.DataFrame(self.edges_list, columns=['source', 'target'])
        # Count the frequency of each country
        freq_df = pd.concat([edges_df['source'], edges_df['target']]).value_counts().reset_index()
        # Keep the top 20 countries
        top_20_countries = freq_df.nlargest(15, 'count')['index'].tolist()
        # Filter edges_df to keep only pairs where both countries are in the top 20
        edges_df = edges_df[edges_df['source'].isin(top_20_countries) & edges_df['target'].isin(top_20_countries)]
        return edges_df

    def country_chord_chart(self):
        hv.extension('bokeh')
        chord = hv.Chord(self.create_edges()).select(value=(1, None))

        # Define your custom colors
        custom_colors = ['#0068c9', '#83c9ff', '#ffabab', '#29b09d', '#7defa1', 'red']

        return chord.opts(
            opts.Chord(
                cmap=custom_colors,  # Use your custom colors
                edge_cmap=custom_colors,
                edge_color=dim('source').str(),
                labels='index',
                node_color=dim('index').str(),
                width=600,
                height=600,
                tools=['tap'],
                toolbar=None
            )
        )

if __name__ == '__main__':
    data = [['Ukraine', 'Deutschland'], ['Deutschland', 'USA'], ['USA', 'Deutschland'], ['Ukraine', 'USA']]
    test = ChordCharts(data)
    print(test.create_edges())
