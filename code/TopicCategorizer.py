import spacy


class TopicCategorizer:
    """
    Die Klasse TopicCategorizer dient zur Kategorisierung von Texten basierend auf ihrem thematischen Inhalt.

    Die Kategorisierung erfolgt durch die Berechnung der Ähnlichkeit zwischen dem gegebenen Text und einer vordefinierten
    Gruppe von Schlüsselwörtern für jede Kategorie. Die Ähnlichkeit wird mittels Wortvektor-Ähnlichkeit berechnet,
    die von Spacy's Sprachmodell 'de_core_news_lg' bereitgestellt wird. Der Wortvektor ist eine mehrdimensionale
    Darstellung eines Worts, die dessen Bedeutung in Bezug auf andere Wörter im Vokabular repräsentiert.
    Die Idee ist, dass Wörter, die in ähnlichen Kontexten vorkommen, ähnliche Bedeutungen haben und daher
    ähnliche Vektoren haben sollten.

    Attribute:
    - nlp_de (Language): Ein Spacy-Sprachmodell für Deutsch.
    - topics (dict): Ein Wörterbuch, das jede Kategorie ihren Schlüsselwörtern zuordnet.
    """

    def __init__(self):

        self.nlp_de = spacy.load('de_core_news_lg')
        self.topics = {
            'Politik': self.nlp_de('Regierung Politiker Wahl Gesetz Bundesrat Parlament Partei Politik Diplomatie'),
            'Lokales': self.nlp_de('Stadt Kanton Gemeinde Bürger Stadtteil Einwohner Dorf Viertel'),
            'Internationales': self.nlp_de('International UNO NATO EU Brexit Vertrag Frieden Krieg Sanktionen '
                                           'Globalisierung Menschenrechte Krieg'),
            'Wirtschaft': self.nlp_de('Wirtschaft Bank Unternehmen Aktien Börse Business BIP Umsatz Investitionen '
                                      'Handel'),
            'Sport': self.nlp_de('Spiel Sport Turnier Spieler Trainer Wettkampf Meisterschaft Stadion Sieg Niederlage '
                                 'WM Handball Fussball'),
            'Kultur': self.nlp_de('Kunst Literatur Film Musik Theater Tanz Mode Fotografie Roman Gedicht Kino'),
            'Wissenschaft & Technik': self.nlp_de('Forschung Wissenschaft Studie Entdeckung Technologie Software '
                                                  'Hardware Internet Ökologie Nachhaltigkeit Energie Umweltschutz Ingeniuer'),
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
    """
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
    """
    doc = categorizer.nlp_de("Tesla stellt neue Batterietechnologie vor: Revolution in der Elektromobilität?")

    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha)
