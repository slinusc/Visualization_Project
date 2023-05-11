import pandas as pd
import plotly.express as px
import geopandas as gpd
import warnings
warnings.filterwarnings('ignore')

# TODO: percentage Bar anpassen

def laender_aufbereitung():
    # Liste mit Ländern auf Deutsch
    with open("C:/Users/andre/Git_ripository/visualization_project/data/de_laender.csv",
              encoding="UTF-8") as laender_de:
        laender_namen_de = [line.strip() for line in
                            laender_de.readlines()]  # Inhalt der Datei zeilenweise in Liste speichern

    # Länderliste auf englisch, alle Länder die in Grafik erkannt werden könnten.
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world_names_en = world["name"].tolist()  # Spalte "name" als Liste ausgeben

    # Vergleich der Ländernamen mithilfe von fuzzywuzzy
    from fuzzywuzzy import process

    deutsch_list = laender_namen_de  # Ihre erste Liste hier
    english_list = world_names_en  # Ihre zweite Liste hier

    result_dict = {}

    for country in deutsch_list:
        match, score = process.extractOne(country, english_list)
        if score > 70:  # Schwellenwert KÖNNTE anpasst werden. BITTE SO LASSEN
            result_dict[country] = match

    # Für dieses Projekt wichtige Länder, die von fuzzywuzzy falsch oder nicht erkannt wurde.
    dict_nicht_erkannt = {'Frankreich': 'France', 'Schweiz': 'Switzerland', 'USA': 'United States of America',
                          'Spanien': 'Spain', 'Deutschland': 'Germany', 'Italien': 'Italy', 'Österreich': 'Austria',
                          'England': 'United Kingdom', 'Kroatien': 'Croatia', 'Süd Afrika': 'South Africa',
                          'Dominikanische Republik': 'Dominican Rep.', 'Griechenland': 'Greece',
                          'Weissrussland': 'Belarus'}
    result_dict.update(dict_nicht_erkannt)

    # Daten, die so der Weltkartengrafik übergeben werden können.
    data = {'Country': []}

    for key, value in result_dict.items():
        data['Country'].append(value)
    return data


def weltkarte(data):
    df = pd.DataFrame(data)

    # Anzahl von jedem Land
    df['Count'] = df.groupby('Country')['Country'].transform('count')

    # Duplikatentfernung
    df = df.drop_duplicates()

    # Dataimport aus naturalearth_lowres um Koordinaten zu erhalten
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Koordinaten jedem land hinzufügen
    merged = df.merge(world, how="left", left_on='Country', right_on='name')

    # Berechung der Schwerpunktkoordinaten
    world['representative_point'] = world['geometry'].representative_point()
    world['lon'] = world['representative_point'].x
    world['lat'] = world['representative_point'].y

    # Merge der DataFrames, basierend auf der Spalte "name" und "Country"
    merged = merged.merge(world[['name', 'lon', 'lat']], how='left', left_on='Country', right_on='name')

    # Przentuale Anzahl Auftreten für Mrkergrössenverhältnisse
    merged['Percentage'] = 100 * merged['Count'] / merged['Count'].sum()

    # Daten für die Kartenvisualisierung vorbereiten
    fig = px.choropleth(merged, locations='name_x', locationmode='country names',
                        color='Percentage', hover_name='Country',
                        hover_data=['Count', 'Percentage'],
                        projection='natural earth',
                        color_continuous_scale='greens')

    # Kartenlayout festlegen
    fig.update_geos(showcountries=True, countrycolor="darkgrey", showocean=True, oceancolor="lightblue",
                    showland=True, landcolor="white", showframe=False)

    fig.update_layout(
        title_text='Anzahl der Auflistungen pro Land',
        showlegend=False,
        geo=dict(
            scope='world',
            projection_type='natural earth'
        ),
        width=900,  # Anpassen der Breite der Figur
        height=700  # Anpassen der Höhe der Figur
    )

    # Karte anzeigen
    fig.show()


if __name__ == '__main__':
    weltkarte(laender_aufbereitung())
