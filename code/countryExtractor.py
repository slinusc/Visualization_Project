import spacy
import csv


class countryExtractor:

    def __init__(self):
        self.nlp_de = spacy.load('de_core_news_sm')
        countries = []
        with open('../data/de_laender.csv', 'r', encoding='UTF-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                countries.append(row[0])
        self.countries = countries

    def get_country(self, text):
        country = []
        for i in self.countries:
            if i in text:
                country.append(i)
        return set(country)


if __name__ == "__main__":
    text = "Deutschland du Spasst, Adrian ist blöd USA, Schweiz ist schön"
    test = countryExtractor()
    print(test.get_country(text))




