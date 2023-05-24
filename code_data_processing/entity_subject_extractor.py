import spacy
import csv

class EntityAndSubjectExtractor:
    """
    Die Klasse EntityFinder dient zur Extraktion von Entitäten aus Texten.
    Personen und Nomen werden als Entitäten betrachtet. Ausschlaggebend ist die POS-Tagging-Annotation von Spacy.
    Es kommt das deutsche Sprachmodell 'de_core_news_sm' zum Einsatz.
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
        Funktioniert nur mit ganzen Sätzen (kein vorheriges Entfernen von Stoppwörtern),
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

