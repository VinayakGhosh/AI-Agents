import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

# 1) defining chunking logic

def chunk_text(text, chunk_size=150, overlap=30):
    chunks=[]
    start=0
    while(start<len(text)):
        end = start+chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += (chunk_size-overlap)
    return chunks


# 2) Dir scanninga and processing

knowledge_dir = '../knowledge_base'
processed_chunks = []

if not os.path.exists(knowledge_dir):
    print(f"Error dir {knowledge_dir} not found")


for filename in os.listdir(knowledge_dir):
    if filename.endswith('txt'):
        file_path = os.path.join(knowledge_dir, filename)

        with open(file_path, "r", encoding='utf-8') as f:
            raw_text = f.read()

        print(f"Reading file name: {filename}...  Total characters: {len(raw_text)}")

        file_chunks = chunk_text(raw_text, chunk_size=100, overlap=30)
        print('file chunks:')
        print(file_chunks)
        print()

        for index, chunk_content in enumerate(file_chunks):
            # skip empty chunks
            if not chunk_content:
                continue
        
        # generate openai embeddings
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=[chunk_content]
            )
        
        # Extract the mathematical vector
        vector = response.data[0].embedding

        # save our structured chunk data locally
        processed_chunks.append({
            "source_file": filename,
            "chunk_index": index,
            "content": chunk_content,
            "embedding": vector
        })

print("\n" + "="*40)
print(f"Ingestion Complete!")
print(f"Total structured chunks generated and embedded: {len(processed_chunks)}")
print(f"Dimensions of first chunk's embedding: {len(processed_chunks[0]['embedding'])}")
print("="*40)
print(processed_chunks)