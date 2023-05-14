import spacy

class TopicCategorizer:

    def __init__(self):
        self.nlp_de = spacy.load('de_core_news_lg')
        self.topics = {
        'Politik': self.nlp_de('Regierung Politiker Wahl Gesetz Bundesrat Parlament Partei Politik Diplomatie'),
        'Lokales': self.nlp_de('Stadt Kanton Gemeinde Bürger Stadtteil Einwohner'),
        'Internationales': self.nlp_de('International UNO NATO EU Brexit Vertrag Frieden Krieg Sanktionen '
                                       'Globalisierung Menschenrechte Krieg'),
        'Wirtschaft': self.nlp_de('Wirtschaft Bank Unternehmen Aktien Börse Business BIP Umsatz Investitionen '
                                  'Handel'),
        'Sport': self.nlp_de('Spiel Sport Turnier Spieler Trainer Wettkampf Meisterschaft Stadion Sieg Niederlage '
                             'WM Handball Fussball'),
        'Kultur': self.nlp_de('Kunst Literatur Film Musik Theater Tanz Bildhauerei Fotografie Roman Gedicht Kino '),
        'Wissenschaft & Technik': self.nlp_de('Forschung Wissenschaft Studie Entdeckung Technologie Software '
                                              'Hardware Internet Ökologie Nachhaltigkeit Energie  Umweltschutz'),
        }

    def categorize(self, text):
        if isinstance(text, list):
            text = " ".join(text)
        doc = self.nlp_de(text)
        similarities = {}

        for category, keywords in self.topics.items():
            similarities[category] = doc.similarity(keywords)

        if similarities:
            most_similar_category = max(similarities, key=similarities.get)
            return most_similar_category

        return "Keine Kategorie gefunden"


if __name__ == "__main__":
    categorizer = TopicCategorizer()
    print(categorizer.categorize("Zins ist ein wichtiges Thema in der Börse."))
    print(categorizer.categorize("Apple stellt neues iPhone-Modell vor: Technische Innovationen begeistern Fans."))
    print(categorizer.categorize("Bundeskanzlerin trifft sich mit US-Präsidenten zur Diskussion über Klimapolitik."))
    print(categorizer.categorize("BVB gewinnt gegen FC Bayern München: Der Kampf um die Bundesliga-Spitze geht weiter."))
    print(categorizer.categorize("Neue Studie zeigt: Klimawandel hat stärkeren Einfluss auf Biodiversität als gedacht."))
    print(categorizer.categorize("Google kauft Start-up: Wirtschaftliche Expansion im Tech-Sektor."))
    print(categorizer.categorize("Literaturpreis geht an unbekannten Autor: Kulturelle Überraschung des Jahres."))
    print(categorizer.categorize("Tesla stellt neue Batterietechnologie vor: Revolution in der Elektromobilität?"))
    print(categorizer.categorize("Finanzminister warnt vor Inflation: Wirtschaftliche Auswirkungen der Pandemie."))
    print(categorizer.categorize("Kunstausstellung im Louvre bricht Besucherrekord: Kulturelles Highlight des Jahres."))
    print(categorizer.categorize("Formel 1: Lewis Hamilton siegt beim Großen Preis von Monaco."))