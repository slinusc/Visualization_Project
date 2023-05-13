import spacy
from collections import Counter

class EntityFinder:

    def __init__(self, headlines: list):
        self.nlp_de = spacy.load('de_core_news_sm')
        self.topics = ["Politik", "Wirtschaft", "Sport", "Kultur", "Wissenschaft", "Technik"]

    def get_most_common_entities(self, n=3):
        entities = Counter()
        for text in self.headlines:
            doc = self.nlp_de(text)
            person_names = [ent.text.lower() for ent in doc.ents if ent.label_ == 'PER']
            full_names = [name.replace("'s", "").title() for name in person_names]
            entities.update(full_names)

            nouns = [token.text.lower() for token in doc if token.pos_ == 'NOUN']
            capitalized_nouns = [noun.title() for noun in nouns]
            entities.update(capitalized_nouns)

        return entities.most_common(n)


if __name__ == "__main__":

    analyser = EntityFinder()

    words = analyser.get_most_common_entities(20)

