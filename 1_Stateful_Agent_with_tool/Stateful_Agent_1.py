from openai import OpenAI
from dotenv import load_dotenv
from tools import tools, get_horoscope
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

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        break

    message_list.append({"role": "user", "content": user_input})

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
            try:
                tool_function = available_tools[item.name]
                args = json.loads(item.arguments)
                result = tool_function(**args)
            except Exception as e:
                result = f"Tool error {e}"

            # Provide function call results to model
            message_list.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": result
            })
    # if not tool_called:
    #     break
    assistant_response = response.output_text
    print("Assistant: ", assistant_response)
    
