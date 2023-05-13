import csv

class CountryExtractor:
    def __init__(self):
        self.countries = set()
        with open('../data/de_laender.csv', 'r', encoding='UTF-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                self.countries.add(row[0])

    def get_country(self, text):
        found_countries = []
        for word in text:
            if word in self.countries:
                found_countries.append(word)
        return list(set(found_countries))


if __name__ == "__main__":
    text = ["Schweden", "du", "Haus", "adrian", "USA", "Schweiz"]
    test = CountryExtractor()
    print(test.get_country(text))
