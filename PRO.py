
text = input("Enter a sentence: ")

# Simple tokenization by splitting on spaces

tokens = text.split()

print("Original text:")

print(text)

print("Tokens:")

for i, token in enumerate (tokens): print(i, "----..... -", token)

print("Total tokens:", len(tokens))