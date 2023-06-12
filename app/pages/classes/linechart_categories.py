import plotly.express as px


class LinechartCategories:
    """
    Diese Klasse bietet Funktionalitäten zum Erstellen von Liniendiagrammen.
    Diese Klasse ist speziell auf Daten zugeschnitten, die Datum und Kategorie als Attribute haben.
    Die Methode 'linechart_categories' gruppiert die Daten nach Datum und Kategorie und zählt dann die Anzahl der
    Einträge in jeder Kategorie für jedes Datum. Das resultierende Liniendiagramm zeigt die Anzahl der Einträge
    in jeder Kategorie im Laufe der Zeit. Jede Kategorie wird in einer unterschiedlichen Farbe dargestellt,
    die durch das Attribut 'color_discrete_map' definiert wird.
    """
    def __init__(self, ):
        pass

    def linechart_categories(self, data):
        # Jede Kategorie erhält eine eindeutige Farbe, die im Diagramm verwendet wird.
        color_discrete_map = {'Politik': '#0068c9', 'Regional': '#83c9ff', 'Sport': 'red',
                              'Wirtschaft': '#ffabab', 'Wissenschaft & Technik': '#29b09d', 'Kultur': '#7defa1'}

        df_grouped = data.groupby(['Datum', 'Kategorie']).size().reset_index(name='Anzahl')
        fig = px.line(df_grouped, x='Datum', y='Anzahl', color='Kategorie', color_discrete_map=color_discrete_map)
        fig.update_layout(
            width=1100
        )
        return fig


if __name__ == '__main__':
    pass
