from openai import OpenAI
from dotenv import load_dotenv
from tools import tools, get_horoscope
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
    "get_horoscope": get_horoscope
}

# Set a strict guardrail against infinite agent loops
MAX_ITERATIONS = 5
iterations = 0

while iterations < MAX_ITERATIONS:
    iterations += 1
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        break

    message_list.append({"role": "user", "content": user_input})

    while True:

        response = client.responses.create(
            model=model,
            tools=tools,
            input=message_list
        )

        message_list += response.output

        tool_called = False 
        for item in response.output:
            if item.type=='function_call':
                tool_called=True

                # Function call logic for every function call
                result = execute_tool(item, available_tools)

                # Provide function call results to model
                message_list.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": result
                })
        if not tool_called:
            break

    assistant_response = response.output_text
    print("Assistant: ", assistant_response)
    print()
    
