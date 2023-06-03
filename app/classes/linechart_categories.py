import plotly.express as px


class LinechartCategories:
    def __init__(self, ):
        pass

    def linechart_categories(self, data):
        df_grouped = data.groupby(['Datum', 'Kategorie']).size().reset_index(name='Anzahl')
        fig = px.line(df_grouped, x='Datum', y='Anzahl', color='Kategorie')
        fig.update_layout(
            width=1100
        )
        return fig


if __name__ == '__main__':
    pass
