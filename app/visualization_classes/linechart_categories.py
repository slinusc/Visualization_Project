import plotly.express as px

class LinechartCategories:
    def __init__(self, selected_date):
        self.selected_date = selected_date

    def linechart_categories(self, data):
        df_grouped = data.groupby(['date', 'article_category']).size().reset_index(name='count')
        fig = px.line(df_grouped, x='date', y='count', color='article_category')
        fig.update_layout(
        shapes=[
            dict(
                type='line',
                yref='paper', y0=0, y1=1,
                xref='x', x0=self.selected_date, x1=self.selected_date,
                line=dict(color='Yellow', width=1)
            )
        ],
        title='Kateorigen erwähnt in Headlines', xaxis_title='Date', yaxis_title='Count')
        return fig
