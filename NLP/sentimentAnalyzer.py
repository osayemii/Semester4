import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download vader_lexicon(Run once)
# nltk.download("vader_lexicon")

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Sample sentences
sentences = [
    "I am extremely happy with the service.",
    "This is the worst product I have ever used.",
    "The movie was okay, not great but not bad either."
]
sentiment = ""

# Analyze sentiment
for sentence in sentences:
    # Doesn'r read a an hashed word in a sentence. "I am extremely #happy with the service."
    # 'happy' won't be read by polarity_scores
    scores = sia.polarity_scores(sentence)
    
    print(f"Sentence: {sentence}")
    print(f"Sentence Score: {scores}")
    
    compound_score = scores['compound']
    
    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    print(f"Overall Sentiment: {sentiment}")