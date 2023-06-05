import time
import pandas as pd
import plotly.graph_objects as go


class WorldMap:

    def __init__(self, data):
        self.data = data
        self.start_time = time.time()

    def erstelle_weltkarte(self):
        # Flatten the data and count occurrences
        flat_list = [item for sublist in self.data for item in sublist]
        df = pd.DataFrame(flat_list, columns=['Country'])
        df = df['Country'].value_counts().reset_index()
        df.columns = ['Country', 'Count']

        # Daten für die Kartenvisualisierung vorbereiten
        fig = go.Figure(data=go.Choropleth(
            locations=df['Country'],
            z=df['Count'],
            locationmode='country names',
            colorscale='Greens',
            colorbar_title="Anzahl",
        ))

        # Kartenlayout
        fig.update_geos(showcountries=True, countrycolor="darkgrey", showocean=True, oceancolor="lightblue",
                        showland=True, landcolor="white", showframe=False)

        fig.update_layout(
            geo=dict(
                scope='world',
                projection_type='natural earth'
            ),
            width=1600,
            height=600
        )

        # Karte anzeigen
        print("Weltkarte", time.time() - self.start_time)
        return fig


if __name__ == '__main__':
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
    karte = WorldMap(data_country)
    karte.erstelle_weltkarte()
    final_tile = time.time() - karte.start_time
    print("Ladezeit für Weltkarte:", final_tile, "Sekunden")
