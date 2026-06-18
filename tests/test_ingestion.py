from src.ingestion.ingestion_pipeline import run_ingestion

chunks = run_ingestion(
    "data/raw_documents/IDB_LESSON_PLAN.pdf"
)

print("Total Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0].page_content[:500])

print("\nMetadata:")
print(chunks[0].metadata)