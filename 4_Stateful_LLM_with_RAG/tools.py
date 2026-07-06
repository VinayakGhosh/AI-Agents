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