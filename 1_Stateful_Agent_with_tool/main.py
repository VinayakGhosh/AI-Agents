from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
client = OpenAI()


response = client.responses.create(
    model=model,
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
