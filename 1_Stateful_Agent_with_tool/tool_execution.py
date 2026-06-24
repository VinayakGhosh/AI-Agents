import json

# function to execute tool call
def execute_tool(tool_call, available_tools):
    tool_name = tool_call.name

    if tool_name not in available_tools:
        return f"Unknown tool: {tool_name}"
    
    print("=" * 50)
    print("Tool:", tool_name)
    print("Arguments:", tool_call.arguments)
    try:
        args = json.loads(tool_call.arguments)
        tool_function = available_tools[tool_name]
        result = tool_function(**args)
        return result
    except Exception as e:
        return f"Tool execution failed: {str(e)}"