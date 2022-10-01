import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = 'i am in a bad mood today but day was good for me'
#nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()
score = (sid.polarity_scores(str(text)))['compound']

if (score > 0):
    label = 'This sentence is Positive'
elif (score==0):
    label = 'This sentence is neutral'
else:
    label = 'This sentence is Negative'

print(label)