import spacy
import csv

class EntityAndSubjectExtractor:
    """

    Die Klasse EntityFinder dient zur Extraktion von Entitäten aus Texten.

    Die Methode extract_entities extrahiert alle Substantive aus einem Text. Die Extraktion erfolgt durch das deutsche
    Sprachmodell 'de_core_news_lg'.

    Die Methode get_people() extrahiert alle Personen aus einem Text. Die Extraktion erfolgt durch den Vergleich der
    Wörter des Textes mit der Liste der Personen des öffentlichen Lebens. Die Liste ist eine Zusammenstellung der 1239
    relevantesten und einflussreichsten Personen des Jahres 2022 aus den Bereichen Politik, Wirtschaft, Sport, Kultur,
    Medien, Wissenschaft und Gesellschaft.

    Die Methode SubjectFinder dient zur Extraktion von Subjekten aus Texten.
    Subjekte sind diejenigen Entitäten, die im Satz das Verb bestimmen. Die Extraktion erfolgt durch die Erkennung der
    Abhängigkeiten zwischen den Wörtern im Satz. Es kommt das deutsche Sprachmodell 'de_core_news_lg' zum Einsatz.

    Attribute:
        nlp_de: Das deutsche Sprachmodell 'de_core_news_lg' von spaCy.
        famous_people: Eine Liste der Personen des öffentlichen Lebens.

    """
    def __init__(self):
        self.nlp_de = spacy.load('de_core_news_lg')
        self.famous_people = {}
        with open('../data/persoenlichkeiten.csv', 'r', encoding='UTF-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                self.famous_people[row[1]] = row[0]

    def extract_entities(self, text):
        if isinstance(text, list):
            text = " ".join(text)
        doc = self.nlp_de(text)
        nouns = [token.lemma_ for token in doc if token.pos_ == 'NOUN']
        return nouns

    def extract_people(self, word_list):
        people = []
        text = " ".join(word_list)
        for person in self.famous_people.keys():
            if person.lower() in text.lower():
                people.append(person)
        return people

    def get_subjects(self, text):
        """
        Achtung:
        Funktioniert nur mit ganzen Sätzen (kein vorheriges Entfernen von Stopwörtern),
        da ansonsten die Abhängigkeiten nicht korrekt erkannt werden.
        """
        if isinstance(text, list):
            text = " ".join(text)
        doc = self.nlp_de(text)
        subjects = [token.lemma_ for token in doc if token.dep_ == 'sb']
        return subjects


if __name__ == "__main__":
    analyser = EntityAndSubjectExtractor()
    text = ["Bundeskanzlerin," "Angela", "Merkel",  "trifft", "sich", "mit", "US-Präsidenten", "Joe", "Biden", "zur",
            "Diskussion", "über", "Klimapolitik."]
    entities = analyser.extract_entities(text)
    subjects = analyser.get_subjects(text)
    people = analyser.extract_people(text)
    #print(f'Entities: {entities}, Subject: {subjects}, People: {people}')
    print(f'People: {people}')

