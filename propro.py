
import tiktoken

text = "Generative AI can create amazing applications."

# GPT-style tokenizer

encoding = tiktoken.get_encoding("cl100k_base")

tokens=encoding.encode(text)

print("Original text:")

print(text)

print("\nToken IDs:")

print(tokens)
print("\nNumber of tokens:")
print(len(tokens))
print("\nDecoded tokens:")

for token_id in tokens:
    token_text = encoding.decode([token_id])
    print(token_id, "->", repr(token_text))