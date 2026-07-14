import spacy

# Load the Englis language model with entity lining support (Assuming an appropriate model)
nlp = spacy.load("en_core_web_sm")

# Sample text
text =  "Apple Inc. is headquartered in Cupertino, California."

# Process the text
doc = nlp(text)

# Print entities with their labels and linked IDs
for ent in doc.ents:
    # Printing the entity, its label, and knowledge base ID if available
    print(f"{ent.text}, {ent.label_}, {getattr(ent, 'kb_id', 'No KB ID')}")