import plotly.express as px
import pandas as pd

class TopicAnalysis:
    """
    Klasse zur Durchführung einer Themenanalyse.
    Diese Klasse akzeptiert einen DataFrame und führt eine Themenanalyse durch.
    Sie erstellt ein Balkendiagramm, das die Top-20-Themen (Entitäten im Header)
    zeigt, die in verschiedenen Medien erwähnt werden.
    """

    def __init__(self, df):
        self.df = df

    def preprocess(self):
        """
        Bereitet den DataFrame für die Themenanalyse vor.
        Die Methode explodiert die 'Entitäten Header' Spalte, filtert dann die Top-20-Entitäten
        und gruppiert sie nach Medium. Die Methode erstellt eine Spalte 'counts', die die Häufigkeit
        jeder Entität im jeweiligen Medium angibt und sortiert den DataFrame entsprechend den Gesamthäufigkeiten.
        """
        column_name = 'Entitäten Header'
        self.df = self.df.explode(column_name)
        top_n = self.df[column_name].value_counts().index[:20]

        self.df = self.df[self.df[column_name].isin(top_n)]
        self.df = self.df.groupby([self.df[column_name], 'Medium']).size().reset_index(name='counts')
        total_counts = self.df.groupby(column_name)['counts'].sum().reset_index(name='total_counts')
        self.df = pd.merge(self.df, total_counts, on=column_name)
        self.df.sort_values(['total_counts', 'Medium'], ascending=[False, True], inplace=True)

    def plot(self):
        # Erzeugt ein Balkendiagramm, das die Ergebnisse der Themenanalyse darstellt.
        self.preprocess()
        column_name = 'Entitäten Header'
        sorted_categories = self.df[column_name].unique().tolist()



        fig = px.bar(self.df, x=column_name, y='counts', color='Medium',
                     labels={column_name: 'Topic', 'Medium': 'Medium', 'counts': 'Anzahl'},
                     height=600,
                     width=1100,
                     category_orders={column_name: sorted_categories})
        return fig



