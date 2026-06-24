# Stateful Agent with Tool

This directory contains a simple example of a stateful conversational agent that can call a tool to fetch horoscopes.

## Files

- `Stateful_Agent_1.py`: Main script for the stateful agent.
- `tools.py`: Defines callable tool metadata and the `get_horoscope` function.
- `tool_execution.py`: Handles execution of tool calls returned by the model.

## High-Level Summary

This example builds a loop where the agent maintains conversation state across turns and can invoke a tool when needed.

- `Stateful_Agent_1.py` initializes a conversation history and available tools.
- It sends the current message history to OpenAI's Responses API.
- If the model issues a function call, the code executes the matching tool from `available_tools`.
- The tool output is appended back into the conversation state so the model can continue the dialogue.
- The conversation continues until the user types `exit`, `quit`, or `bye`.

## How it works

1. The user enters text at the prompt.
2. The message is appended to `message_list`.
3. The script calls `client.responses.create(...)` with the full message history and tool definitions.
4. If the model returns a `function_call`, `execute_tool` runs the tool and returns the result.
5. The response from the tool is added to the conversation history as function call output.
6. The loop continues until the model produces a normal assistant response.

## Requirements

- Python 3.11+ (or latest supported version)
- `openai` Python package
- `python-dotenv` package
- A valid OpenAI API key stored in a `.env` file or environment variable

## Setup

1. Create a `.env` file in this directory or the project root.
2. Add your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

3. Install dependencies:

```bash
pip install -r ../requirements.txt
```

If dependencies are not installed via `requirements.txt`, install directly:

```bash
pip install openai python-dotenv
```

## Run

From the `1_Stateful_Agent_with_tool` directory:

```bash
python Stateful_Agent_1.py
```

Type a question or ask for a horoscope. Example:

```text
You: What is the horoscope for Aries?
```

Then type `exit`, `quit`, or `bye` to end the session.

## Extending this Example

- Add more tool definitions to `tools.py`
- Register new functions in `available_tools` inside `Stateful_Agent_1.py`
- Improve the conversation prompt or developer instructions
- Add validation and error handling for tool arguments
