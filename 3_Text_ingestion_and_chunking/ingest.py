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



# 3) Vector search mechanics

def compute_dot_product(vector_a, vector_b):
    return sum(a*b for a,b in zip(vector_a, vector_b))

def query_knowledge_base(user_query, vault_data, top_k=2):
    # 1. Generate embedding for the incoming user query
    query_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=[user_query]
    )

    query_vector = query_response.data[0].embedding

    # 2. score every chunk in our vault using dot product similarity
    
    scored_chunks=[]

    for chunk in vault_data:
        similarity = compute_dot_product(query_vector, chunk["embedding"])
        scored_chunks.append((similarity, chunk))
        

    # 3. Sort by similarity score in decending order
    scored_chunks.sort(key=lambda x: x[0], reverse=True)

    # 4. Return the top K closest matches
    return scored_chunks[:top_k]

# --- Test Our Search Implementation ---
query = "What happens if a health check fails during deployment?"
print(f"\nUser Query: '{query}'")
print("Searching vault...")

result = query_knowledge_base(query, processed_chunks, top_k=1)

for score, chunk in result:
    print(f"\n[Match Score: {score:.4f}] Found in file: {chunk['source_file']}")
    print(f"Content:\n{chunk['content']}")