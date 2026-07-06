from ingestion_and_chunking import query_knowledge_base, vault_data

# tool definition for search_engineering_handbook

tools = [
    {
        "type": "function",
        "name": "search_engineering_handbook",
        "description": "policies regarding deployments, health checks, database migrations, and rollbacks.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The specific search query or question about engineering policy.",
                },
            },
            "required": ["query"],
        },

    }
]


def search_engineering_handbook(query):
    # using vector search function to get top matches
    results =  query_knowledge_base(query, vault_data, top_k=2)

    # Threshold filter to filter out relevant results and discard irrelvant results
    THRESHOLD=3

    relevant_chunks = []
    for score, chunk in results:
        if score >= THRESHOLD:
            relevant_chunks.append(chunk['content'])
    
    if not relevant_chunks:
        return 'No relevant engineering policies found for this query'
    
    return "\n---\n".join(relevant_chunks)