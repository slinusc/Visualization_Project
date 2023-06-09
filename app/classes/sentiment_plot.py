import matplotlib.pyplot as plt
import numpy as np

class SentimentObjectivityPlots:
    def __init__(self, sentiment_list, subjectivity_list):
        self.sentiment_list = sentiment_list
        self.subjectivity_list = subjectivity_list

        self.sentiment_labels = ['< -0.5', '< 0', '< 0.5', '>= 0.5']
        self.subjectivity_labels = ['< 0.2', '>= 0.2']

    def count_subjectivity(self):
        counts = [0, 0]
        for subjectivity in self.subjectivity_list:
            if subjectivity < 0.2:
                counts[0] += 1
            else:
                counts[1] += 1
        return counts

    def count_sentiment(self):
        counts = [0, 0, 0, 0]
        for sentiment in self.sentiment_list:
            if sentiment < -0.5:
                counts[0] += 1
            elif sentiment < 0:
                counts[1] += 1
            elif sentiment < 0.5:
                counts[2] += 1
            else:
                counts[3] += 1
        return counts

    def plot(self):
        sentiment_counts = self.count_sentiment()
        subjectivity_counts = self.count_subjectivity()

        cmap = plt.cm.get_cmap('Blues')
        colors = cmap(np.linspace(0.3, 1, 4))

        fig, axs = plt.subplots(2, 1, figsize=(10, 15))

        axs[0].pie(sentiment_counts, labels=self.sentiment_labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        axs[0].set_title('Sentiment')
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        axs[0].add_artist(centre_circle)

        axs[1].pie(subjectivity_counts, labels=self.subjectivity_labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
        axs[1].set_title('Subjectivity')
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        axs[1].add_artist(centre_circle)

        axs[0].axis('equal')
        axs[1].axis('equal')

        plt.tight_layout()
        plt.show()

if '__main__' == __name__:

    sentiments = [0.1, -0.3, 0.5, 0.8, -0.6]
    subjectivities = [0.1, 0.3, 0.5, 0.8, 0.6]
    plotter = SentimentObjectivityPlots(sentiments, subjectivities)
    plotter.plot()
