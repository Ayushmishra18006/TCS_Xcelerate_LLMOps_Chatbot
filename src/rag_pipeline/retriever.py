from src.vector_store.chroma_client import (
    ChromaClient
)

from src.embeddings.embedding_generator import (
    EmbeddingGenerator
)


class Retriever:

    def __init__(self):

        self.embedder = EmbeddingGenerator()

        self.db = ChromaClient()

    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ):

        query_embedding = (
            self.embedder.generate_embedding(
                query
            )
        )

        results = (
            self.db.collection.query(
                query_embeddings=[
                    query_embedding.tolist()
                ],
                n_results=top_k
            )
        )

        return results