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
            'Kultur': self.nlp_de('Kunst Literatur Film Musik Theater Tanz Bildhauerei Fotografie Roman Gedicht Kino '),
            'Wissenschaft & Technik': self.nlp_de('Forschung Wissenschaft Studie Entdeckung Technologie Software '
                                                  'Hardware Internet Ökologie Nachhaltigkeit Energie  Umweltschutz'),
            }

    def categorize(self, text):

        """
        Kategorisiert einen gegebenen Text.

        Der Text wird zuerst in eine Dokumentdarstellung umgewandelt, die vom Spacy-Sprachmodell bereitgestellt wird.
        Danach wird die Ähnlichkeit zwischen dem Text und den Schlüsselwörtern jeder Kategorie berechnet.
        Die Kategorie, die die höchste Ähnlichkeit aufweist, wird als die Kategorie des Textes angenommen.

        Args:
        - text (str): Der zu kategorisierende Text als String oder Liste

        Returns:
        - str: Die Kategorie des Textes. Wenn keine Kategorie gefunden wurde, wird der String "Keine Kategorie gefunden" zurückgegeben.
        """

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
