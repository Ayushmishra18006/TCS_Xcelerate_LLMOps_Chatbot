from src.vector_store.chroma_client import (
    ChromaClient
)

client = ChromaClient()

client.reset_collection()

print("Collection reset successfully.")