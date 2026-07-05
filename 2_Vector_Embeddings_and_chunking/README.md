# RAG Vector Creation

This folder contains a small test script for creating text embeddings with the OpenAI API. The script loads your API key from a `.env` file, sends sample text to the `text-embedding-3-small` model, and prints basic details about the generated vector.

## Files

- `embed_test.py` - Generates an embedding for a sample sentence and prints the vector size plus the first few values.

## Setup

Create a `.env` file in the project root with your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

Install the required packages if needed:

```bash
pip install openai python-dotenv
```

## Run

```bash
python embed_test.py
```
