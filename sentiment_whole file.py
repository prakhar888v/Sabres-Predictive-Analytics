from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
from nltk import tokenize

analyzer = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyzer.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))
    for _ in range(900): print("-", end='')
    print()

file_path = 'opening night speculation.csv'

with open(file_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter='\n')
    line_count = 0
    sentences = []
    for row in csv_reader:
        # sentiment_analyzer_scores(str(row)) if str(row).strip() != '' else 1
        if str(row).strip() != '':
            sentences += tokenize.sent_tokenize(str(row).strip())

i = len(sentences)-1
while(i>=0):
    if sentences[i] == '' or sentences[i] == '[]':
        del sentences[i]
    i-=1

sentences_with_the_name_lazar = 0
for i in range(1,len(sentences)):
    if 'lazar' in sentences[i] or 'Lazar' in sentences[i]:
        sentiment_analyzer_scores(','.join(sentences[i-1:i+2]))
