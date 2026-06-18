import chromadb


class ChromaClient:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./data/chroma_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="university_documents"
            )
        )

    def add_documents(
        self,
        ids,
        documents,
        embeddings,
        metadatas
    ):

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

    def count(self):

        return self.collection.count()

    def reset_collection(self):

        try:
            self.client.delete_collection(
                name="university_documents"
            )
        except Exception:
            pass

        self.collection = (
            self.client.get_or_create_collection(
                name="university_documents"
            )
        )