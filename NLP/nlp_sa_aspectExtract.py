# pip install textblob
# python -m textblob.download_corpora

from textblob import TextBlob
from collections import defaultdict

reviews = [
    "The quality of the product is outstanding, but the price is too high.",
    "Customer service was helpful. The usability of the product is poor."
]

aspects = ["quality", "price", "customer service", "usability"]

sentiments = defaultdict(lambda: {"positive": 0, "negative": 0, "neutral": 0})

for review in reviews:
    blob = TextBlob(review)
    # print(blob.sentences)

    for sentence in blob.sentences:
        polarity = sentence.sentiment.polarity
        # print(polarity)
        text = str(sentence).lower()
        # print(text)
        
        for aspect in aspects:
            if aspect.lower() in text:
                if polarity > 0:
                    sentiments[aspect]["positive"] += 1
                elif polarity < 0:
                    sentiments[aspect]["negative"] += 1
                else:
                    sentiments[aspect]["neutral"] += 1

for aspect, counts in sentiments.items():
    print(f"{aspect}: {counts}")