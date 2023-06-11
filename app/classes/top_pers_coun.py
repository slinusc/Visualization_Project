import plotly.express as px
import pandas as pd


class StackedBarPlot:
    """
    Die StackedBarPlot-Klasse erstellt ein gestapeltes Balkendiagramm aus einem gegebenen DataFrame.
    Die Klasse unterstützt Filteroptionen für die Visualisierung nach Ländern oder Personen.
    """

    def __init__(self, df, filter):
        self.df = df
        self.filter = filter

    def preprocess(self):
        """
        Bereitet die Daten für das Diagramm vor. Es werden die Top-10-Länder oder Top-20-Personen ermittelt
        und die Daten entsprechend gefiltert und sortiert.
        """
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
        """
        Erzeugt ein gestapeltes Balkendiagramm basierend auf den verarbeiteten Daten.
        In Abhängigkeit vom Filterkriterium werden entweder gestapelte Balkendiagramme für die Top-10-Länder oder
        Top-20-Personen erzeugt. Die Methode ruft zunächst die `preprocess`-Methode auf, um die Daten vorzubereiten.
        Anschliessend wird ein Plotly-Express-Balkendiagramm erzeugt, das die Anzahl der Kategorien nach Ländern
        oder Personen darstellt.
        """
        self.preprocess()
        column_name = 'Länder' if self.filter == 'country' else 'Personen'
        sorted_categories = self.df[column_name].unique().tolist()

        color_discrete_map = {'Politik': '#0068c9', 'Regional': '#83c9ff', 'Sport': 'red',
                              'Wirtschaft': '#ffabab', 'Wissenschaft & Technik': '#29b09d', 'Kultur': '#7defa1'}
        # 0d47a1', '#2196f3', '#00bcd4', '#4dd0e1
        if self.filter == 'country':
            fig = px.bar(self.df, y=column_name, x='counts', color='Kategorie',
                         color_discrete_map=color_discrete_map,
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



