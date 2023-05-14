import pandas as pd
import plotly.express as px
import time
import ast

# TODO: percentage Bar anpassen
def get_countries(date):
    start_time_countries = time.time()
    selected_string = data_country.loc[data_country['datum'] == date, 'Country'].values[0]
    selected_dict = ast.literal_eval(selected_string)  # Umwandlung des String in ein Dictionary
    df = pd.DataFrame(selected_dict)
    print("get_countries", time.time() - start_time_countries)
    return df


def weltkarte(data):
    start_time_weltkarte = time.time()
    df = pd.DataFrame(data)

    # Duplikate zusammenfassen und 'Count'-Werte summieren
    df = df.groupby('Country').sum().reset_index()

    # Daten für die Kartenvisualisierung vorbereiten
    fig = px.choropleth(df, locations='Country',
                        locationmode='country names',
                        color='Count',
                        title='Count by Country',
                        color_continuous_scale=px.colors.sequential.Greens)

    # Kartenlayout
    fig.update_geos(showcountries=True, countrycolor="darkgrey", showocean=True, oceancolor="lightblue",
                    showland=True, landcolor="white", showframe=False)

    fig.update_layout(
        title_text='Anzahl der Auflistungen pro Land',
        showlegend=False,
        geo=dict(
            scope='world',
            projection_type='natural earth'
        ),
        width=900,
        height=700
    )

    # Formatierung anpassen Kacheln
    fig.update_traces(hovertemplate='<b>Land</b>: %{location}<br><b>Anzahl</b>: %{z}')
    # Beschriftung ändern des Farbbalkens
    fig.update_layout(coloraxis_colorbar_title='Anzahl')

    # Karte anzeigen
    print("weltkarte", time.time() - start_time_weltkarte)
    fig.show()


    # TODO evtl das integrieren???????
    """
    # Barplot für Verteilung
    bar_df = df.sort_values(by='Count', ascending=False).head(10)  # Nur die 10 größten Werte
    fig_bar = px.bar(bar_df, x='Country', y='Count', title='Verteilung des Counts pro Land',
                     color='Count', color_continuous_scale=px.colors.sequential.Greens)
    fig_bar.update_layout(xaxis_title='Land', yaxis_title='Count')
    fig_bar.update_traces(marker=dict(color='green', width=1),
                          selector=dict(type='bar'))
    fig_bar.show()
    """


if __name__ == '__main__':
    start_time = time.time()
    data_country = pd.read_csv(
        'C:/Users/andre/Desktop/ZHAW Unterricht (Nicht Cloud)/Semester 2/Visualisation and Data Science Storytelling/Semestertask/data_country.csv')
    weltkarte(get_countries("2022-01-12"))
    completed_time = time.time()
    final_tile = completed_time - start_time
    print("Ladezeit für Weltkarte:", final_tile, "Sekunden")
