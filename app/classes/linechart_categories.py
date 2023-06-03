import plotly.express as px


class LinechartCategories:
    def __init__(self, ):
        pass

    def linechart_categories(self, data):
        df_grouped = data.groupby(['date', 'article_category']).size().reset_index(name='count')
        fig = px.line(df_grouped, x='date', y='count', color='article_category')
        fig.update_layout(
            xaxis_title='Datum', yaxis_title='Anzahl',
            width=1100  # Change the width,
        )
        return fig

if __name__ == '__main__':
    pass