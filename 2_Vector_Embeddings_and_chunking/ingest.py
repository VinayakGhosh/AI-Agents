def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start<len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        # Move the window forward by chunk_size minus the overlap
        start += (chunk_size - overlap)
    return chunks

# Test document simulating a company policy or system manual
sample_document = """
Welcome to the Engineering Handbook. 
All microservices deployed to production must implement standard health checks at the '/healthz' endpoint.
Database migrations must be executed during the maintenance window on Tuesdays between 02:00 and 04:00 UTC.
For deployments, we use a blue-green strategy to minimize downtime. 
If a rollback is required, the deployment pipeline will automatically revert traffic to the previous stable container image within 60 seconds of a failed health check.
Emergency hotfixes can bypass the standard window but require approval from the Director of Engineering.
"""


chunks = chunk_text(sample_document, chunk_size=150, overlap=30)

print(f"Total chunks created: {len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print(chunk.strip())