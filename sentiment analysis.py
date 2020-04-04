from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv

analyzer = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyzer.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))
    for _ in range(900): print("-", end='')
    print()


file_path = 'Posts repo.csv'

with open(file_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter='\n')
    line_count = 0
    for row in csv_reader:
        sentiment_analyzer_scores(str(row))


