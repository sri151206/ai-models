# Chat Application - Simple interactive chatbot

from openai import OpenAI

client = OpenAI(
    api_key="GRQ_API_KEY",
    base_url="https://api.groq.com/openai/v1",
)

MODEL = "openai/gpt-oss-20b"

print("=== Simple Chatbot ===")
print("Type 'quit' to exit\n")

messages = [{"role": "system", "content": "You are a friendly assistant. Keep answers short."}]

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # Add user message to conversation
    messages.append({"role": "user", "content": user_input})

    # Get AI response
    response = client.chat.completions.create(
        model=MODEL, temperature=0.7, messages=messages
    )
    reply = response.choices[0].message.content

    # Add AI reply to conversation
    messages.append({"role": "assistant", "content": reply})

    print(f"Bot: {reply}\n")