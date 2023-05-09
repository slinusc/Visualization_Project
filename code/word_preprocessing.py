import string
import spacy

class headline_preprocessing:
    def __init__(self, text):
        self.text = text
        self.nlp_de = spacy.load('de_core_news_sm')

    def preprocess_text(self, text):
        text = self.remove_punctuation(text)
        text = self.remove_stopwords(text)
        text = self.lemmatize_words(text)
        return text

    def preprocess_headlines(self, headlines):
        preprocessed_headlines = [self.preprocess_text(headline) for headline in headlines]
        return preprocessed_headlines

    def remove_punctuation(self, text):
        translator = str.maketrans("", "", string.punctuation)
        return text.translate(translator)

    def remove_stopwords(self, text):
        doc = self.nlp_de(text)
        filtered_tokens = [token for token in doc if not token.is_stop]
        filtered_text = " ".join(token.text for token in filtered_tokens)
        return filtered_text

    def lemmatize_words(self, text):
        doc = self.nlp_de(text)
        lemmatized_tokens = [token.lemma_ for token in doc]
        lemmatized_text = " ".join(lemmatized_tokens)
        return lemmatized_text


if __name__ == "__main__":
    import pandas as pd

    headlines = pd.read_csv("C:/Users/linus/Downloads/daten_aijan_filtered.csv")

    # einzelne Schlagzeile bereinigen
    single_headline = headlines['titel'][0]
    preprocessor = headline_preprocessing(single_headline)
    preprocessed_single_headline = preprocessor.preprocess_text(single_headline)
    print("Einzelne bereinigte Schlagzeile:", preprocessed_single_headline)

    print(headlines.head(10))
    # Liste von Schlagzeilen bereinigen
    all_preprocessed_headlines = [preprocessor.preprocess_text(headline) for headline in headlines['titel']]
    print("Alle bereinigten Schlagzeilen:", all_preprocessed_headlines)
