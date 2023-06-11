import pandas as pd
import plotly.subplots as sp
import plotly.graph_objects as go


class NewspaperCategoryPlot:
    """
    Die NewspaperCategoryPlot Klasse erstellt mehrere Liniendiagramme, die die Häufigkeit von Kategorien über die Zeit
    in verschiedenen Zeitungen darstellen. Wenn 'Alle' in der Liste der Kategorien ausgewählt ist,
    wird kein Filter auf die Kategorien angewendet. Jedes Liniendiagramm wird in einem separaten Subplot dargestellt,
    mit maximal acht Subplots.
    """
    def __init__(self, df, category):
        self.df = df
        self.category = category

    def plot_newspaper_category(self):
        # Überprüfen, ob 'Alle' in der Liste der ausgewählten Kategorien vorhanden ist.
        # Wenn 'Alle' ausgewählt ist, bedeutet das, dass wir keinen Filter auf die Kategorie anwenden wollen.
        if 'Alle' in self.category:
            # Wenn 'Alle' ausgewählt ist, verwenden wir den gesamten DataFrame ohne Filter.
            df_category = self.df
        else:
            # Wenn 'Alle' nicht ausgewählt ist, filtern wir den DataFrame nach den ausgewählten Kategorien.
            df_category = self.df[self.df['Kategorie'].isin(self.category)]

        # Liste der Zeitungen
        newspapers = df_category['Medium'].unique()

        # Begrenzt die Anzahl der Zeitungen auf 8, falls es mehr gibt
        if len(newspapers) > 8:
            newspapers = newspapers[:8]

        fig = sp.make_subplots(rows=2, cols=4, subplot_titles=newspapers)

        for i, newspaper in enumerate(newspapers):
            df_newspaper = df_category[df_category['Medium'] == newspaper]
            df_grouped = df_newspaper.groupby('Datum').size().reset_index(name='Anzahl')

            # 2 Reihen und 4 Spalten von Subplots
            row = i // 4 + 1
            col = i % 4 + 1

            fig.add_trace(go.Scatter(x=df_grouped['Datum'], y=df_grouped['Anzahl'], mode='lines', name=newspaper,
                                     line=dict(color='#1f77b4')
                                     ), row=row, col=col)

        fig.update_layout(showlegend=False, plot_bgcolor='white')
        fig.update_xaxes(showgrid=False, gridcolor='white')
        fig.update_yaxes(showgrid=False, gridcolor='white')
        fig.update_layout(showlegend=False, plot_bgcolor='white', width=1100, )

        return fig

if __name__ == '__main__':
    df = pd.read_csv('../../data/without_content.tsv.xz', sep='\t', compression='xz')
    plotter = NewspaperCategoryPlot(df, 'Politik')
    plotter.plot_newspaper_category()
