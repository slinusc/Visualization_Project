import matplotlib.pyplot as plt
from wordcloud import WordCloud


class theWordCloud:
    def __init__(self, word_list):
        self.word_list = word_list

    def generate_wordcloud(self):
        text = " ".join(self.word_list)
        wordcloud = WordCloud(width=800, height=400, collocations=False, background_color="white").generate(text)
        return wordcloud

    def display_wordcloud(self, wordcloud):
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        return plt

if __name__ == '__main__':
    word_lists = ['Leitzinserhöhung', 'Ende', 'Schweizerinn', 'Quali-Ende', 'Tabakinitiative', 'Tür', 'Werbeverbot']
    wordcloud_generator = theWordCloud(word_lists)
    generated_wordcloud = wordcloud_generator.generate_wordcloud()
    wordcloud_generator.display_wordcloud(generated_wordcloud)