import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Apple Inc. was founded bySteve Jobs and Steve Wozniak in 1976."

# NER using spacy
doc = nlp(text)

# Print named entities, entity labels and position
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")