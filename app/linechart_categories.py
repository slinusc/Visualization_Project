import plotly.express as px

class LinechartCategories:
    def __init__(self):
        pass

    @staticmethod
    def linechart_categories(data):
        df_grouped = data.groupby(['date', 'article_category']).size().reset_index(name='count')
        fig = px.line(df_grouped, x='date', y='count', color='article_category')
        fig.update_layout(title='Line Chart of Medium Names', xaxis_title='Date', yaxis_title='Count')
        return fig
