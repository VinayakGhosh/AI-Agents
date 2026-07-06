from openai import OpenAI
from dotenv import load_dotenv
from tools import tools, search_engineering_handbook
from tool_execution import execute_tool
import os
import json

load_dotenv()
model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
client = OpenAI()

# created a stateful agent which responses 

message_list=[
    {"role": "developer", "content": "You are a helpful funny assistant. You answer to user queries, but also make jokes along the way."}
]

available_tools = {
    "search_engineering_handbook": search_engineering_handbook
}

# Set a strict guardrail against infinite agent loops
MAX_ITERATIONS = 5
iterations = 0