from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def product_review(sentence):
    score = sia.polarity_scores(sentence)
    
    print(f"Sentence: {sentence}")
    print(f"Score: {score}")
    
    compound_score = score['compound']
    sentiment = ""
    
    if compound_score >= 0.05:
        sentiment = "Positive"
    elif compound_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    print(f"Sentiment: {sentiment}")
    
    
inpVal = input("Enter a review: ")
product_review(inpVal)