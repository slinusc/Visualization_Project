import spacy
import difflib
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from textblob_de import TextBlobDE as TextBlob
from wordcloud import WordCloud

class HeadlineAnalyser:

    def __init__(self, headlines: list):
        self.headlines = headlines
        self.nlp_de = spacy.load('de_core_news_sm')
        self.topics = ["Politik", "Wirtschaft", "Sport", "Kultur", "Wissenschaft", "Technik", "Gesundheit", "Lifestyle"]

    def get_most_common_entities(self, n=10):
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

    def get_categorized_headlines(self):
        categorized_headlines = {topic: [] for topic in self.topics}

        for headline in self.headlines:
            similarities = [difflib.SequenceMatcher(None, headline.lower(), topic.lower()).ratio() for topic in
                            self.topics]
            best_match_topic = self.topics[similarities.index(max(similarities))]
            categorized_headlines[best_match_topic].append(headline)

        return categorized_headlines

    def get_topic_sentiments(self):
        topic_sentiments = {}
        for topic, headlines in self.get_categorized_headlines().items():
            sentiment_scores = []
            for headline in headlines:
                headline_blob = TextBlob(headline)
                sentiment_scores.append(headline_blob.sentiment.polarity)
            topic_sentiments[topic] = sentiment_scores
        return topic_sentiments

    def get_word_cluster(self, words):
        text = " ".join(schlagzeile for schlagzeile in words)
        wordcloud = WordCloud(collocations=False, background_color="white").generate(text)
        # Zeigt die Wortwolke mit Matplotlib an
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

if __name__ == "__main__":

    headlines = pd.read_csv("C:/Users/linus/Downloads/daten_aijan_filtered.csv")
    headlines = headlines['titel'].head(100)
    analyser = HeadlineAnalyser(headlines)
    words = analyser.get_most_common_entities(20)
    words = [tupel[0] for tupel in words]
    analyser.get_word_cluster(words)
