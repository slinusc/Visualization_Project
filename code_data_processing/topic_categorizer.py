import spacy


class TopicCategorizer:
    """
    Die Klasse TopicCategorizer dient zur Kategorisierung von Texten basierend auf ihrem thematischen Inhalt.

    Die Kategorisierung erfolgt durch die Berechnung der Ähnlichkeit zwischen dem gegebenen Text und einer vordefinierten
    Gruppe von Schlüsselwörtern für jede Kategorie. Die Ähnlichkeit wird mittels Wortvektor-Ähnlichkeit berechnet,
    die von Spacy's Sprachmodell 'de_core_news_lg' bereitgestellt wird. Der Wortvektor ist eine mehrdimensionale
    Darstellung eines Worts, die dessen Bedeutung in Bezug auf andere Wörter im Vokabular repräsentiert.
    Die Idee ist, dass Wörter, die in ähnlichen Kontexten vorkommen, ähnliche Bedeutungen haben und daher
    ähnliche Vektoren haben sollten. Die Ähnlichkeit zwischen zwei Wörtern wird als Kosinus-Ähnlichkeit berechnet,
    die den Kosinus des Winkels zwischen zwei Vektoren darstellt. Je näher der Kosinus dem Wert 1 ist, desto ähnlicher
    sind die Wörter. Es kommt das deutsche Sprachmodell 'de_core_news_lg' zum Einsatz. Dieses muss vorher mit
    'python -m spacy download de_core_news_sm heruntergeladen werden. Das Modell ist für die
    Verwendung mit Python 3.8 optimiert.

    Attribute:
    - nlp_de (Language): Spacy-Sprachmodell für Deutsch.
    - topics (dict): Ein Dictionary, das jede Kategorie ihren Schlüsselwörtern zuordnet.
    """

    def __init__(self):

        self.nlp_de = spacy.load('de_core_news_lg')
        self.topics = {
            'Politik': self.nlp_de('Regierung Politiker Wahl Gesetz Bundesrat Parlament Partei Politik Diplomatie '
                                   'International UNO NATO EU Vertrag Frieden Krieg Sanktionen'
                                   'Staat Globalisierung Menschenrechte Krieg Politik'),
            'Regional': self.nlp_de('Stadt Kanton Gemeinde Bürger Stadtteil Einwohner Dorf Viertel Strasse '
                                    'Region lokal Anwohner Quartier Regional Gemeinderat Gemeindeversammlung'),
            'Wirtschaft': self.nlp_de('Wirtschaft Bank Unternehmen Aktien Börse Business BIP Umsatz '
                                      'Investitionen Industrie Handel Finanzen Preis Wachstum Firma CEO Dividende'),
            'Sport': self.nlp_de('Spiel Sport Turnier Spieler Trainer Wettkampf Meisterschaft Stadion Sieg Niederlage '
                                 'WM Handball Fussball Tennis Basketball Eishockey Formel1 Volleyball Ballsport'),
            'Kultur': self.nlp_de('Kunst Literatur Film Musik Theater Tanz Mode '
                                  'Fotografie Roman Gedicht Kino Contest Star Kulinarik Kultur'),
            'Wissenschaft & Technik': self.nlp_de('Forschung Wissenschaft Studie Entdeckung Technologie Technik '
                                                  'Software Hardware Internet Ökologie Energie Hochschule'
                                                  'Umweltschutz Ingenieur Informatik Medizin Universität'
                                                  'Chemie Physik Künstliche Intelligenz AI Digitalisierung Robotik'),
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

    print(categorizer.categorize("Apple stellt neues iPhone-Modell vor: Technische Innovationen begeistern Fans."))
    print(categorizer.categorize("Bundeskanzlerin trifft sich mit US-Präsidenten zur Diskussion über Klimapolitik."))
    print(
        categorizer.categorize("BVB gewinnt gegen FC Bayern München: Der Kampf um die Bundesliga-Spitze geht weiter."))
    print(
        categorizer.categorize("Neue Studie zeigt: Klimawandel hat stärkeren Einfluss auf Biodiversität als gedacht."))
    print(categorizer.categorize("Google kauft Start-up: Wirtschaftliche Expansion im Tech-Sektor."))
    print(categorizer.categorize("Literaturpreis geht an unbekannten Autor: Kulturelle Überraschung des Jahres."))
    print(categorizer.categorize("Tesla stellt neue Batterietechnologie vor: Revolution in der Elektromobilität?"))
    print(categorizer.categorize("Finanzminister warnt vor Inflation: Wirtschaftliche Auswirkungen der Pandemie."))
    print(categorizer.categorize("Kunstausstellung im Louvre bricht Besucherrekord: Kulturelles Highlight des Jahres."))
    print(categorizer.categorize("Formel 1: Lewis Hamilton siegt beim Großen Preis von Monaco."))


