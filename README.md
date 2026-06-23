# AI Agents

Exploring different AI agent architectures with LLMs.

## Setup

```bash
pip install -r requirements.txt
```

Create `.env` file:
```env
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4o-mini
```

## Running Agents

```bash
cd 1_Stateful_Agent_with_tool
python Stateful_Agent_1.py
```

## Structure

Each folder contains a different agent implementation. The `1_Stateful_Agent_with_tool` folder includes a stateful agent example that:

- keeps conversation history across multiple turns,
- uses a callable `get_horoscope` tool defined in `tools.py`, and
- handles tool invocation and tool output with the OpenAI Responses API.
