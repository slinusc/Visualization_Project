import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class TextPreprocessing:

    """
    Diese Klasse dient der Vorverarbeitung von Texten.
    Sie entfernt alle Sonderzeichen und Stopwords.
    Auf Stemming wurde wegen der Grösse des Datensatzes und
    Performancegründen verzichtet.
    """

    def __init__(self):
        self.stops = set(stopwords.words('german'))

    def preprocess_text(self, text):
        text = self.remove_special_chars(text)
        text = self.remove_stopwords(text)
        return text

    def remove_special_chars(self, text):
        no_tags_text = re.sub(r'<.*?>', ' ', text)
        cleaned_text = re.sub(r'\W+', ' ', no_tags_text)
        return cleaned_text

    def remove_stopwords(self, data):
        text = word_tokenize(data)
        text_without_stopwords = []
        for i in text:
            if i not in self.stops:
                text_without_stopwords.append(i)
        return text_without_stopwords


if __name__ == "__main__":
    text = '<tx><ld><p>Die schwedische Notenbank stemmt sich mit einer kräftigen Zinsanhebung gegen die hohe Inflation im Land. Der Leitzins steigt um einen ganzen Prozentpunkt auf 1,75 Prozent, wie die Reichsbank am Dienstag in Stockholm mitteilte.</p></ld><p><au>SDA Import</au></p><p>Es ist die dritte Zinsanhebung in diesem Jahr. Analysten hatten zwar mit einer weiteren Straffung der Geldpolitik gerechnet, mehrheitlich allerdings einen Schritt um 0,75 Prozentpunkte erwartet. Schon eine solche Anhebung wäre eine sehr deutliche Straffung gewesen.</p><p>Die Inflation sei zu hoch, begründete die Notenbank ihren Zinsentscheid. Die Teuerung schwäche die Kaufkraft der Haushalte und erschwere den Konsumenten und Unternehmen die Finanzplanung. Zuletzt war die Teuerung in Schweden auf knapp zehn Prozent gestiegen. Das liegt deutlich über dem Zielwert der Reichsbank von etwa zwei Prozent. Die Währungshüter kündigten für den Jahresverlauf weitere Zinsanhebungen an.</p><p>(SDA)</p></tx>'
    test = TextPreprocessing()
    print(test.preprocess_text(text))

