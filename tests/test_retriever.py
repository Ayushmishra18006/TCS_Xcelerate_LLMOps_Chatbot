from src.rag_pipeline.retriever import (
    Retriever
)

retriever = Retriever()

query = "What are ACID properties?"

results = retriever.retrieve(
    query=query,
    top_k=5
)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

for i in range(len(documents)):

    print("\n" + "=" * 80)

    print(f"Result {i+1}")

    print(
        f"Page: {metadatas[i].get('page')}"
    )

    print(
        f"Distance: {distances[i]}"
    )

    print()

    print(
        documents[i][:700]
    )