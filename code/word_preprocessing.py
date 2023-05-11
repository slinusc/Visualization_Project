import string
import spacy
import re

class headline_preprocessing:
    def __init__(self):
        self.nlp_de = spacy.load('de_core_news_sm')

    def preprocess_text(self, text):
        text = self.remove_special_chars(text)
        text = self.remove_stopwords(text)
        text = self.lemmatize_words(text)
        return text

    def remove_special_chars(self, text):
        no_tags_text = re.sub(r'<.*?>', ' ', text)
        cleaned_text = re.sub(r'\W+', ' ', no_tags_text)
        return cleaned_text


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
    text = '<tx><ld><p>Die schwedische Notenbank stemmt sich mit einer kräftigen Zinsanhebung gegen die hohe Inflation im Land. Der Leitzins steigt um einen ganzen Prozentpunkt auf 1,75 Prozent, wie die Reichsbank am Dienstag in Stockholm mitteilte.</p></ld><p><au>SDA Import</au></p><p>Es ist die dritte Zinsanhebung in diesem Jahr. Analysten hatten zwar mit einer weiteren Straffung der Geldpolitik gerechnet, mehrheitlich allerdings einen Schritt um 0,75 Prozentpunkte erwartet. Schon eine solche Anhebung wäre eine sehr deutliche Straffung gewesen.</p><p>Die Inflation sei zu hoch, begründete die Notenbank ihren Zinsentscheid. Die Teuerung schwäche die Kaufkraft der Haushalte und erschwere den Konsumenten und Unternehmen die Finanzplanung. Zuletzt war die Teuerung in Schweden auf knapp zehn Prozent gestiegen. Das liegt deutlich über dem Zielwert der Reichsbank von etwa zwei Prozent. Die Währungshüter kündigten für den Jahresverlauf weitere Zinsanhebungen an.</p><p>(SDA)</p></tx>'
    test = headline_preprocessing()
    print(test.remove_special_chars(text))

