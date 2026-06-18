from src.vector_store.chroma_client import (
    ChromaClient
)

client = ChromaClient()

print(
    "Documents Stored:",
    client.count()
)