import pandas as pd
import plotly.graph_objects as go
import time


def weltkarte(data):
    # Ausgabe der interaktiven Weltkarte.
    start_time_weltkarte = time.time()
    # Flatten the data and count occurrences
    flat_list = [item for sublist in data for item in sublist]
    df = pd.DataFrame(flat_list, columns=['Country'])
    df = df['Country'].value_counts().reset_index()
    df.columns = ['Country', 'Count']

    # Daten für die Kartenvisualisierung vorbereiten
    fig = go.Figure(data=go.Choropleth(
        locations=df['Country'],
        z=df['Count'],
        locationmode='country names',
        colorscale='Greens',
        colorbar_title="Count",
    ))

    # Kartenlayout
    fig.update_geos(showcountries=True, countrycolor="darkgrey", showocean=True, oceancolor="lightblue",
                    showland=True, landcolor="white", showframe=False)

    fig.update_layout(
        title_text='Ländernennungen',
        geo=dict(
            scope='world',
            projection_type='natural earth'
        ),
        width=900,
        height=700
    )

    # Karte anzeigen
    print("Weltkarte", time.time() - start_time_weltkarte)
    fig.show()


if __name__ == '__main__':
    start_time = time.time()
    data_country = [['Switzerland', 'Germany'],
                    ['Germany'],
                    ['France', 'Germany', 'Germany'],
                    ['Austria', 'Australia'],
                    ['Netherlands', 'Iraq', 'Iran', 'United States of America', 'Switzerland', 'Russia', 'Israel',
                     'Croatia', 'Syria',
                     'Congo', 'Lebanon', 'Sweden', 'France', 'Argentina', 'Finland', 'India', 'Australia', 'Egypt',
                     'China', 'Germany',
                     'Spain', 'Ukraine', 'Libya', 'Turkey', 'Canada', 'Zambia', 'Burundi', 'Tanzania', 'Vietnam',
                     'Botswana', 'Poland',
                     'Antarctica', 'Pakistan', 'Denmark', 'Italy', 'Belize', 'Japan', 'Guatemala', 'Iceland',
                     'Luxembourg', 'Estonia',
                     'Austria', 'Brazil', 'Bulgaria', 'Morocco', 'Belarus', 'Portugal', 'Taiwan', 'Philippines',
                     'Colombia', 'Ecuador',
                     'Panama', 'Mexico', 'Greece', 'Romania', 'Hungary', 'Kenya', 'Somalia'],
                    ['Qatar', 'Qatar'],
                    ['Qatar'],
                    ['Switzerland', 'Switzerland', 'Switzerland', 'Switzerland'],
                    ['Switzerland'],
                    ['Switzerland']]

    weltkarte(data_country)
    completed_time = time.time()
    final_tile = completed_time - start_time
    print("Ladezeit für Weltkarte:", final_tile, "Sekunden")