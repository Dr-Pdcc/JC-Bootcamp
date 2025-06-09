import spacy

# Load the spaCy English language model.
nlp = spacy.load("en_core_web_sm")

# Define a list of garden path sentences.
# Two sentences were chosen as common garden path examples.
gardenpathSentences = [
    "Fat people eat accumulates.",
    "The florist sent the flowers was pleased."
]

# List of predifined garden path sentences
predefined_sentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Add suggested garden path sentences to my proposed ones
gardenpathSentences.extend(predefined_sentences)

# Initialise the set for unique entity labels.
unique_labels = set()


# Tokenize each sentence and perform named entity recognition.
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    print("Tokens:", [token.orth_ for token in doc])
    print("Entities:")
    if doc.ents:
        for ent in doc.ents:
            explanation = spacy.explain(ent.label_)
            print(f"  {ent.text} ({ent.label_}): {explanation}")
            unique_labels.add(ent.label_)
    else:
        print("  No entities found.")
    print("\n")

# Print a summary of unique entity labels and their explanations.
print("Summary of unique entity labels and their explanations:")
for label in unique_labels:
    print(f"{label}: {spacy.explain(label)}")

'''Comments on two entities looked up:

1. Entity: GPE ("Mississippi")
    - Explanation: "Countries, cities, states."
    - Did it make sense? Yes. "Mississippi" is a USA state, so categorising it as a geopolitical entity (GPE) is appropriate.

 2. Entity: PERSON ("Mary")
    - Explanation: "People, including fictional."
    - Did it make sense? Yes. "Mary" is a common personal name, and spaCy correctly categorises it as a PERSON.
'''