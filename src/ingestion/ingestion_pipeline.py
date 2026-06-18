from src.ingestion.pdf_loader import load_pdf
from src.ingestion.chunking import chunk_documents


def run_ingestion(pdf_path):

    documents = load_pdf(pdf_path)

    chunks = chunk_documents(documents)

    return chunks