# Rules
positive_rules = ['good', 'interesting', 'love', 'amazing', 'affordable', 'quality', 'nice']
negative_rules = ['bad', 'worst', 'hate', 'dislike', 'frustrating', 'disappointed', "don't like", "do not like"]

def product_review(sentence):
    positive_count = 0
    negative_count = 0

    text = str(sentence).lower()

    for rule in positive_rules:
        if rule in text:
            positive_count += text.count(rule)

    # handles multi-word phrases like "don't like"
    for rule in negative_rules:
        if rule in text:
            negative_count += text.count(rule)

    if positive_count > negative_count:
        sentiment = "Positive"
    elif negative_count > positive_count:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"Sentence: {sentence}")
    print(f"Sentiment: {sentiment}")


inpVal = input("Enter a review: ")
product_review(inpVal)

