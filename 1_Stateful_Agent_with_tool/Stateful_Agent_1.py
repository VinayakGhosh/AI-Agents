from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
client = OpenAI()

messages=[
    {"role": "developer", "content": "You are a helpful funny assistant. You answer to user queries, but also make jokes along the way."}
]

while True:
    user_input = input("You: ")
    messages.append({"role": "user", "content": user_input})

    response = client.responses.create(
        model=model,
        input=messages
    )

    assistant_response = response.output_text
    print("Assistant: ", assistant_response)
    print()
    messages.append({"role": "assistant", "content": assistant_response})
