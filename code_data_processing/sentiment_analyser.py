from textblob_de import TextBlobDE as TextBlob

class SentimentAnalyser:

    """
    Polarität: TextBlob berechnet die Polarität eines Textes,
    um zu bestimmen, ob der Text positiv, negativ oder neutral ist.
    Der Polaritätswert liegt zwischen -1 und 1, wobei -1 für eine
    stark negative Aussage steht, 1 für eine stark positive
    Aussage und 0 für eine neutrale Aussage.

    Subjektivität: TextBlob berechnet die Subjektivität eines Textes,
    um zu bestimmen, inwieweit der Text eine subjektive Meinung oder
    eine objektive Tatsache darstellt. Der Wert für Subjektivität
    liegt zwischen 0 und 1, wobei 0 für eine objektive Aussage
    steht und 1 für eine stark subjektive Aussage.
    """

    def __init__(self):
        pass

    def get_topic_sentiments_polarity(self, text):
        if isinstance(text, list):
            text = " ".join(text)
        headline_blob = TextBlob(text)
        return headline_blob.polarity

    def get_topic_subjectivity(self, text):
        if isinstance(text, list):
            text = " ".join(text)
        headline_blob = TextBlob(text)
        return headline_blob.subjectivity

if __name__ == "__main__":
    test = SentimentAnalyser()
    print(test.get_topic_sentiments_polarity("Finanzminister warnt vor Inflation: Wirtschaftliche Auswirkungen der Pandemie."))
    print(test.get_topic_sentiments_polarity("Die strahlende Sonne und der klare, blaue Himmel machen diesen Tag zu "
                                             "einem perfekten Moment für einen erholsamen Spaziergang im Park."))