from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import re
from nltk.util import ngrams
import pandas as pd

nltk.download('stopwords')
nltk.download('punkt')

data_path = 'C:\\Users\\prakh\\Documents\\Sabres project\\hfboard_comments1.csv'
df = pd.read_csv(data_path,usecols=['Messages','Likes'])

for message in df['Messages']:

    # example_sent = "This is a sample sentence, showing off the stop words filtration."
    # example_sent.translate(None, string.punctuation)

    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(message)

    # filtered_sentence = [w for w in word_tokens if not w in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    filtered_string = ' '.join(filtered_sentence)

    filtered_string = filtered_string.lower()
    filtered_string = re.sub(r'[^a-zA-Z0-9\s]', ' ', filtered_string)
    tokens = [token for token in filtered_string.split(" ") if token != ""]
    output = list(ngrams(tokens, 3))

    print(output)
    for _ in range(900): print("-", end='')

    print()

