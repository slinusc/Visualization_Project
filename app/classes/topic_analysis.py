import pandas as pd
import plotly.graph_objects as go

class TopicAnalysis:

    def __int__(self):
        pass

    @staticmethod
    def most_common_words(word_list, n_words):
        """
        Function to get the most common words in a dataframe
        :param word_list: List of words
        :param n_words: Number of words to return
        :return: List with the most common words
        """
        df = pd.DataFrame(sum(word_list, []), columns=['word'])
        words = df['word'].value_counts().index.tolist()[:n_words]
        count = df['word'].value_counts().tolist()[:n_words]
        return words, count

    def plot_most_common_words(self, word_list, n_words):
        words, counts = self.most_common_words(word_list, n_words)
        words = [word.capitalize() for word in words]
        fig = go.Figure(data=[go.Bar(
            x=words,
            y=counts
        )])
        fig.update_layout(xaxis_title='Worte', yaxis_title='Anzahl', width=1100, height=500)
        return fig


if __name__ == '__main__':

    data = [['aa', 'aa', 'bb'],['cc', 'dd', 'ee'],['ff', 'gg', 'hh', 'gg', 'qq', 'gg']]
    test = TopicAnalysis()
    print(test.most_common_words(data, 2))
    test.plot_most_common_words(data, 2)