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

count = 0

while count <4:
    user_input = input("You: ")
    message_list.append({"role": "user", "content": user_input})

    response = client.responses.create(
        model=model,
        tools=tools,
        input=message_list
    )

    message_list += response.output

    tool_called = False 
    for item in response.output:
        tool_called=True
        if item.type=='function_call':
            if item.name=='get_horoscope':

                # Function logic for get horoscope
                sign=json.loads(item.arguments)["sign"]
                print('sign = ', sign)
                horoscope = get_horoscope(sign)

                # Provide function call results to model
                message_list.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": horoscope
                })
    
    if tool_called:
        response = client.responses.create(
            model = model,
            instructions='respond properly using the function output',
            tools=tools,
            input = message_list
        )

    assistant_response = response.output_text
    print("Assistant: ", assistant_response)
    
    message_list+=response.output
    count +=1
    print("count: ", count)
    print()
print(message_list)
