import itertools
import pandas as pd
import holoviews as hv
from holoviews import opts, dim


class ChordCharts:
    """
    Diese Klasse ermöglicht die Erstellung von Chord Diagrammen zur Darstellung von Beziehungen zwischen verschiedenen
    Teilen eines Ganzen. Sie ist besonders nützlich zur Visualisierung von Beziehungen und Interaktionen zwischen
    verschiedenen Ländern, was in geopolitischen oder sozioökonomischen Analysen Anwendung findet oder zur Darstellung
    von Relationen verschiedener Personen.
    Die Klasse wird mit einem DataFrame initialisiert, der die zu visualisierenden Beziehungen repräsentiert. Sie
    enthält die Methode `create_edges`, die eine Liste von Paaren von miteinander verbundenen Elementen erzeugt und
    diese Liste filtert, um nur die 15 am häufigsten auftretenden Elemente zu behalten.
    Die Methode `country_chord_chart` erstellt das eigentliche Chord Diagramm unter Verwendung der `holoviews`
    Bibliothek und der `bokeh` Erweiterung zur Visualisierung. Knoten repräsentieren in diesem Diagramm verschiedene
    Länder oder Personen und Kanten repräsentieren Verbindungen zwischen ihnen.
    """

    def __init__(self, data):
        self.data = data
        self.edges_list = []

    def create_edges(self):
        for connection in self.data:
            for pair in itertools.combinations(connection, 2):
                self.edges_list.append(pair)
        edges_df = pd.DataFrame(self.edges_list, columns=['source', 'target'])
        # Zählen der Häufigkeit der einzelnen Länder
        freq_df = pd.concat([edges_df['source'], edges_df['target']]).value_counts().reset_index()
        # Behalten der 20 wichtigsten Länder
        top_20_countries = freq_df.nlargest(15, 'count')['index'].tolist()
        # Filter edges_df, um nur Paare zu behalten, bei denen beide Länder in den Top 20 sind
        edges_df = edges_df[edges_df['source'].isin(top_20_countries) & edges_df['target'].isin(top_20_countries)]
        return edges_df

    def country_chord_chart(self):
        hv.extension('bokeh')
        chord = hv.Chord(self.create_edges()).select(value=(1, None))

        #  Eigenen Farbpalette
        custom_colors = ['#0068c9', '#83c9ff', '#ffabab', '#29b09d', '#7defa1', 'red']

        return chord.opts(
            opts.Chord(
                cmap=custom_colors,
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
