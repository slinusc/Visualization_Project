import timeit

import spacy


class EntityFinder:

    def __init__(self):
        self.nlp_de = spacy.load('de_core_news_sm')

    def extract_entities(self, text):
        if isinstance(text, list):
            text = " ".join(text)
        doc = self.nlp_de(text)
        # nouns_and_persons = [(token.text) for token in doc if token.pos_ == 'NOUN' or token.ent_type_ == 'PER']
        nouns_and_persons = [(token.lemma_) for token in doc if token.pos_ == 'NOUN' or token.ent_type_ == 'PER']
        return nouns_and_persons


if __name__ == "__main__":
    analyser = EntityFinder()
    text = ["Sag", "reist", "Und", "sage", "wer", "Diese", "alte", "leicht",
            "abgeänderte", "Redewendung", "lässt", "Mitglieder", "Bundesrats",
            "anwenden", "Beispielsweise", "Reise", "jährliche", "Sitzung", "ausserhalb", "Bundesratszimmers"]
    words = analyser.extract_entities(text)
    print(words)
