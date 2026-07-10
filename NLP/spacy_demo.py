import spacy

nlp = spacy.load("en_core_web_sm")

# 1. Raw Text Input
text = """Natural Language Processing (NLP) is one of the most exciting fields in Artificial Intelligence.
Students are learning how computers understand human language by processing text efficiently."""

print("="*70)
print("RAW TEXT")
print("="*70)
print(text)

# Process text
doc = nlp(text)

# 2. Tokenization
print("\n")
print("="*70)
print("STEP 1: TOKENIZATION")
print("="*70)

tokens = [token.text for token in doc]

print(tokens)

# 3. Text Normalization

print("\n")
print("="*70)
print("STEP 2: TEXT NORMALIZATION")
print("="*70)

normalized = [token.text.lower() for token in doc]
print(normalized)


# 4. Stopword Removal

print("\n")
print("="*70)
print("STEP 3: STOPWORD REMOVAL")
print("="*70)

clean_words = [
    token.text.lower()
    for token in doc
    if not token.is_stop and not token.is_punct
]
print(clean_words)


# 5. POS Tagging

print("\n")
print("="*70)
print("STEP 4: PART OF SPEECH TAGGING")
print("="*70)

for token in doc:
    print(f"{token.text:20} {token.pos_:10}")
    

# Final Prepared text

print("\n")
print("="*70)
print("FINAL PREPROCESSED TEXT")
print("="*70)

final_text = " ".join(clean_words)

print(final_text)
