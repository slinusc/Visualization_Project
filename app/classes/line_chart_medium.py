import pandas as pd
import plotly.subplots as sp
import plotly.graph_objects as go

class NewspaperCategoryPlot:
    def __init__(self, df, category):
        self.df = df
        self.category = category

    def plot_newspaper_category(self):
        # Filtern Sie den DataFrame nach der spezifischen Kategorie
        if self.category != 'Alle':
            df_category = self.df[self.df['article_category'] == self.category]
        else:
            df_category = self.df

        # Liste der Zeitungen
        newspapers = df_category['medium_name'].unique()

        # Begrenzen Sie die Anzahl der Zeitungen auf 8, falls es mehr gibt
        if len(newspapers) > 8:
            newspapers = newspapers[:8]

        # Erzeugen Sie eine subplot Figur mit 2 Reihen und 4 Spalten (für 8 Zeitungen)
        fig = sp.make_subplots(rows=2, cols=4, subplot_titles=newspapers)

        # Fügen Sie für jede Zeitung ein Diagramm hinzu
        for i, newspaper in enumerate(newspapers):
            # Filtern Sie den DataFrame nach der spezifischen Zeitung
            df_newspaper = df_category[df_category['medium_name'] == newspaper]

            # Gruppieren Sie den DataFrame nach Datum und zählen Sie die Anzahl der Artikel
            df_grouped = df_newspaper.groupby('date').size().reset_index(name='count')

            # Bestimmen Sie die Position des Diagramms auf der subplot Figur
            row = i // 4 + 1
            col = i % 4 + 1

            # Erstellen Sie ein Liniendiagramm für die Zeitung und fügen Sie es der subplot Figur hinzu
            fig.add_trace(go.Scatter(x=df_grouped['date'], y=df_grouped['count'], mode='lines', name=newspaper), row=row, col=col)

        # Legen Sie die Titel der subplot Figur fest
        fig.update_layout(showlegend=False, plot_bgcolor='white')

        # Setze die Hintergrundfarbe der Achsen auf Weiß und entferne die Gitterlinien
        fig.update_xaxes(showgrid=False, gridcolor='white')
        fig.update_yaxes(showgrid=False, gridcolor='white')
        fig.update_layout(showlegend=False, plot_bgcolor='white', width=1100)

        return fig

if __name__ == '__main__':
    df = pd.read_csv('../../data/without_content.tsv.xz', sep='\t', compression='xz')
    plotter = NewspaperCategoryPlot(df, 'Politik')
    plotter.plot_newspaper_category()
