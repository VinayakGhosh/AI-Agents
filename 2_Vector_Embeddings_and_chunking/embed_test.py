from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

# The text we want to convert into numbers
text_to_embed = "AI agents are changing how we build software."

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=[text_to_embed]
)

# Extract the mathematical vector
vector = response.data[0].embedding

print(f"Vector generated successfully!")
print(f"Total dimensions (number of floats): {len(vector)}")
print(f"First 5 numbers of the vector: {vector[:5]}")