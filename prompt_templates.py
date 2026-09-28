# Prompt Templates - Using variables in prompts

from openai import OpenAI

client = OpenAI(
    api_key="GRQ_API_KEY",
    base_url="https://api.groq.com/openai/v1",
)

MODEL = "openai/gpt-oss-20b"

# --- Prompt Template using f-string ---
topic = input("Enter a topic: ")
audience = input("Enter the target audience: ")

system_prompt = "You are a helpful teacher."
user_prompt = f"Explain {topic} in 2 lines for {audience}."

response = client.chat.completions.create(
    model=MODEL,
    temperature=0.2,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
)

print("Topic:", topic)
print("Audience:", audience)
print("Response:", response.choices[0].message.content)