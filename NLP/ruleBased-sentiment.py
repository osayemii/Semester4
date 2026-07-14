# Define lists of positive and negative sentiment words
negative_words = ['angry', 'disappointed', 'frustrated']
positive_words = ['happy', 'pleased', 'delighted']

# Assuming positive words

def analyze_sentiment(text):
    positive_counts = 0
    negative_counts = 0
    
    # tokenize the text into words
    words = text.split()
    
    # Count positive and negtive words in the text
    for word in words:
        if word.lower() in positive_words:
            positive_counts += 1
        elif word.lower() in negative_words:
            negative_counts += 1
            
    # Determine the sentiment based on the counts
    if positive_counts > negative_counts:
        return 'Positive Sentiment'
    elif negative_counts > positive_counts:
        return 'Negative Sentiment'
    else:
        return 'Neutral Sentiment'
    
    
# Example text
text = "I am very happy with the service, but disappointed with the delivery time and that got me frustrated."

# comma, fullstop and other punctuation are attached to the word and that 
# makes it excluded from the rule. 'frustrated.' is not 'frustrated'
# Apply the analyze_sentiment function and print result
sentiment = analyze_sentiment(text)
print(sentiment)