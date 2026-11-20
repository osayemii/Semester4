import nltk
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from sklearn.datasets import fetch_20newsgroups

# Download the nltk tokenization resource
nltk.download('punkt')

# Load the 20 newsgroups dataset
# subset='all' -> loads both the training and testing portions
newsgroups = fetch_20newsgroups(
    subset='all',
    remove=('headers', 'footers', 'quotes')
)

# Tokenize the text data
tokenized_text = [
    word_tokenize(text)
    for text in newsgroups.data
]

# Train the Word2Vec model
word2vec_model = Word2Vec(
    sentences=tokenized_text,
    
    # vector_size=100: each word is represented using 100 word
    vector_size=100,
    
    # window=5: examine up to 5 words before and after a target word
    window=5,
    
    # min_count=1: Include word that appear at least once
    min_count=1,
    
    # workers=4: Uses 4 CPU worker threads for training
    workers=4
)

# Save or load the trained model

'''# Save model
word2vec_model.save('word2vec_model.bin')

# Load model 
word2vec_model = Word2Vec.load('word2vec_model.bin')'''

# Get the vector representation of a word
vector = word2vec_model.wv['example']

# Display the word vector
print(vector)