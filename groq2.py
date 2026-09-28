from groq import Groq
import os

if not os.environ.get("GROQ_API_KEY"):
    raise SystemExit("GROQ_API_KEY is not set. Set it in your environment before running this script.")

client = Groq()
completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Explain why fast inference is critical for reasoning models"
        }
    ]
)
print(completion.choices[0].message.content)
