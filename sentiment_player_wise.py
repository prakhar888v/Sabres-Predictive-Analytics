from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
from nltk import tokenize
import pandas as pd
import os
from statistics import mean

analyzer = SentimentIntensityAnalyzer()
sentiment_l =  [[[] for _ in range(8)] for _ in range(7)]

def sentiment_analyzer_scores(sentence):
    score = analyzer.polarity_scores(sentence)
    return score['compound']
    # print("{:-<40} {}".format(sentence, str(score)))
    # for _ in range(900): print("-", end='')
    # print()

file_path = 'data_final.csv'
days = ['Today', 'Yesterday','Monday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

df = pd.read_csv(file_path)
df = df.query("Week == 'Week4'")

for i,day in enumerate(days):
    temp_df = df.query(f'Day_of_Week =="{day}"')['messages']
    for message in temp_df:
        message = os.linesep.join([s for s in str(message).splitlines() if s.strip("\r\n")])
        message = ' '.join(message.split())
        if 'lazar' in message.lower() or 'curtis' in message.lower():
            sentiment_l[0][i].append(sentiment_analyzer_scores(message))
        if 'jeff' in message.lower() or 'skinner' in message.lower():
            sentiment_l[1][i].append(sentiment_analyzer_scores(message))
        if 'sobotka' in message.lower() or 'vladimir' in message.lower():
            sentiment_l[2][i].append(sentiment_analyzer_scores(message))
        if 'scandella' in message.lower() or 'marco' in message.lower():
            sentiment_l[3][i].append(sentiment_analyzer_scores(message))
        if 'rasmus' in message.lower() or 'risto' in message.lower() or 'ristolainen' in message.lower():
            sentiment_l[4][i].append(sentiment_analyzer_scores(message))
        if 'connor' in message.lower() or 'sheary' in message.lower():
            sentiment_l[5][i].append(sentiment_analyzer_scores(message))
        if 'jack' in message.lower() or 'eichel' in message.lower() or 'eichs' in message.lower():
            sentiment_l[6][i].append(sentiment_analyzer_scores(message))

for i in range(7):
    for j in range(8):
        sentiment_l[i][j] = round(mean(sentiment_l[i][j]),3) if len(sentiment_l[i][j]) >= 1 and sentiment_l[i][j] != None  else 0


sentiment_l.insert(0, days)

sentiment_l[0].insert(0, 'Day/Player')
sentiment_l[1].insert(0, 'Lazar')
sentiment_l[2].insert(0, 'Skinner')
sentiment_l[3].insert(0, 'Sobotka')
sentiment_l[4].insert(0, 'Scandella')
sentiment_l[5].insert(0, 'Risto')
sentiment_l[6].insert(0, 'Sheary')
sentiment_l[7].insert(0, 'Eichel')

mx = len(max((sub[0] for sub in sentiment_l),key=len))

for row in sentiment_l:
    print(" ".join(["{:<{mx}}".format(ele,mx=mx) for ele in row]))