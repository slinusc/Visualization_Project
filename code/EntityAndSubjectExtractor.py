import spacy


class EntityAndSubjectExtractor:
    """
    Die Klasse EntityFinder dient zur Extraktion von Entitäten aus Texten.
    Personen und Nomen werden als Entitäten betrachtet. Ausschlaggebend ist die POS-Tagging-Annotation von Spacy.
    Es kommt das deutsche Sprachmodell 'de_core_news_sm' zum Einsatz.
    """
    def __init__(self):
        self.nlp_de = spacy.load('de_core_news_sm')

    def extract_entities(self, text):
        if isinstance(text, list):
            text = " ".join(text)
        doc = self.nlp_de(text)
        # nouns_and_persons = [(token.text) for token in doc if token.pos_ == 'NOUN' or token.ent_type_ == 'PER']
        nouns_and_persons = [(token.lemma_) for token in doc if token.pos_ == 'NOUN' or token.ent_type_ == 'PER']
        return nouns_and_persons

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
    text = "Bundeskanzlerin trifft sich mit US-Präsidenten zur Diskussion über Klimapolitik."
    entities = analyser.extract_entities(text)
    subjects = analyser.get_subjects(text)
    print(f'entities: {entities}, Subjekt: {subjects}')
