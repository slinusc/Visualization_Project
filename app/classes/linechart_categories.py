import plotly.express as px


class LinechartCategories:
    def __init__(self, ):
        pass

    def linechart_categories(self, data):

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
