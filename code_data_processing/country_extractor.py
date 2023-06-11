import csv


class CountryExtractor:
    """
    Extrahiert Länder aus einem Text und übersetzt diese in die englische Sprache. Dafür vergleicht die Methode
    get_country() die Wörter des Textes mit der Länderliste. Die Methode country_translation() übersetzt die
    gefundenen Länder in die englische Sprache. Die Länderliste wurde aus dem Wikipedia-Artikel "Liste der Staaten der
    Erde" extrahiert und mit der Google Translate übersetzt. Die Übersetzungen wurden manuell korrigiert.

    Attribute:
        country_en_de_dict: Ein Wörterbuch mit den Ländern als Schlüssel und den englischen Übersetzungen als Werte.
    """
    def __init__(self):
        self.country_en_de_dict = {}
        with open('../data/countries_en_de.csv', 'r', encoding='UTF-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                self.country_en_de_dict[row[1]] = row[0]

    def get_country(self, text):
        found_countries = []
        for word in text:
            if word in self.country_en_de_dict.keys():
                found_countries.append(word)
        return list(set(found_countries))

    def country_translation(self, country_list):
        translation_list = []
        for i in country_list:
            translation_list.append(self.country_en_de_dict[i])
        return translation_list


if __name__ == "__main__":
    text = ["Schweden", "du", "Haus", "adrian", "USA", "Schweiz"]
    country_list = ["Schweden", "USA", "Schweiz", "Russland", "Dschibuti"]
    test = CountryExtractor()
    print(test.get_country(text))
    print(test.country_translation(country_list))