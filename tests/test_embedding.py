from src.ingestion.ingestion_pipeline import (
    run_ingestion
)

from src.embeddings.embedding_generator import (
    EmbeddingGenerator
)

chunks = run_ingestion(
    "data/raw_documents/IDB_LESSON_PLAN.pdf"
)

embedder = EmbeddingGenerator()

embedding = embedder.generate_embedding(
    chunks[0].page_content
)

print(
    "Vector Dimension:",
    len(embedding)
)

print(
    "First 10 Values:"
)

print(
    embedding[:10]
)