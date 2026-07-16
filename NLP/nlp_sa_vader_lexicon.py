import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon (Run once)
# nltk.download("vader_lexicon")

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Sample sentences
sentences = [
    "I am extremely happy with the service.",
    "This is the worst product I have ever used.",
    "The movie was okay, not great but not bad either."
]

# Analyze sentiment
for sentence in sentences:
    scores = sia.polarity_scores(sentence)

    print(f"Sentence: {sentence}")
    print(f"Sentiment Scores: {scores}")

    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"Overall Sentiment: {sentiment}")
