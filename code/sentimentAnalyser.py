from textblob_de import TextBlobDE as TextBlob

class sentimentAnalyser:

    def __init__(self):
        pass

    def get_topic_sentiments(self, text):
        headline_blob = TextBlob(text)
        return headline_blob.sentiment.polarity

if __name__ == "__main__":
    test = sentimentAnalyser()
    text = "Die schwedische Notenbank stemmt sich schön mit einer kräftigen Zinsanhebung gegen die hohe Inflation im Land. Der Leitzins steigt um einen ganzen Prozentpunkt auf 1,75 Prozent."
    print(test.get_topic_sentiments(text))