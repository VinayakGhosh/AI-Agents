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