from src.ingestion.ingestion_pipeline import (
    run_ingestion
)

from src.embeddings.embedding_generator import (
    EmbeddingGenerator
)

from src.vector_store.chroma_client import (
    ChromaClient
)

chunks = run_ingestion(
    "data/raw_documents/IDB_LESSON_PLAN.pdf"
)

embedder = EmbeddingGenerator()

texts = [
    chunk.page_content
    for chunk in chunks
]

embeddings = embedder.generate_embeddings(
    texts
)

client = ChromaClient()

client.add_documents(
    ids=[
        str(i)
        for i in range(len(chunks))
    ],
    documents=texts,
    embeddings=embeddings,
    metadatas=[
        chunk.metadata
        for chunk in chunks
    ]
)

print(
    f"Stored {len(chunks)} chunks successfully."
)