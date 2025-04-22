# meaning_collapse_demo.py

import random

# Define a "quantum word" with multiple possible meanings
quantum_word = {
    "光": ["light", "enlightenment", "wave", "particle", "speed"]
}

# Define different 'context observers'
contexts = {
    "physics": ["wave", "particle", "speed"],
    "philosophy": ["light", "enlightenment"],
    "art": ["light", "color", "mood"],
}

def collapse_meaning(word, context):
    possible = contexts.get(context, [])
    if not possible:
        # If context unknown, pick random meaning
        return random.choice(quantum_word[word])
    return random.choice(possible)

# Example usage
word = "光"

for context in ["physics", "philosophy", "art", "unknown"]:
    meaning = collapse_meaning(word, context)
    print(f"In context '{context}', '{word}' collapses to: {meaning}")
