import os
import numpy as np

from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# ---------------------------------------------------------
# SETTINGS
# ---------------------------------------------------------

DOCUMENT_FOLDER = "documents"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# ---------------------------------------------------------
# LOAD EMBEDDING MODEL
# ---------------------------------------------------------

print("Loading embedding model...")

embedding_model = SentenceTransformer(EMBEDDING_MODEL)

print("Embedding model loaded successfully.")


# ---------------------------------------------------------
# READ TEXT FILE
# ---------------------------------------------------------

def read_txt_file(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# ---------------------------------------------------------
# READ PDF FILE
# ---------------------------------------------------------

def read_pdf_file(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# ---------------------------------------------------------
# LOAD DOCUMENTS
# ---------------------------------------------------------

def load_documents():

    documents = []

    if not os.path.exists(DOCUMENT_FOLDER):

        print("Documents folder not found.")

        return documents

    print("\nScanning documents folder...")

    for filename in os.listdir(DOCUMENT_FOLDER):

        file_path = os.path.join(
            DOCUMENT_FOLDER,
            filename
        )

        # TEXT FILE
        if filename.lower().endswith(".txt"):

            print("Reading:", filename)

            text = read_txt_file(file_path)

        # PDF FILE
        elif filename.lower().endswith(".pdf"):

            print("Reading:", filename)

            text = read_pdf_file(file_path)

        else:

            continue

        if text.strip():

            documents.append(
                {
                    "filename": filename,
                    "text": text
                }
            )

    print(
        "Documents loaded:",
        len(documents)
    )

    return documents


# ---------------------------------------------------------
# CREATE TEXT CHUNKS
# ---------------------------------------------------------

def create_chunks(
    text,
    chunk_size=500,
    overlap=100
):

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(
            words[start:end]
        )

        if chunk.strip():

            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# ---------------------------------------------------------
# BUILD KNOWLEDGE BASE
# ---------------------------------------------------------

def build_knowledge_base():

    print("\nBuilding knowledge base...")

    documents = load_documents()

    chunks = []

    for document in documents:

        document_chunks = create_chunks(
            document["text"]
        )

        for chunk in document_chunks:

            chunks.append(
                {
                    "filename": document["filename"],
                    "text": chunk
                }
            )

    if not chunks:

        print("No document chunks found.")

        return [], None

    print(
        "Total chunks created:",
        len(chunks)
    )

    # Extract text from chunks
    texts = [
        item["text"]
        for item in chunks
    ]

    print("\nCreating embeddings...")

    embeddings = embedding_model.encode(
        texts,
        convert_to_numpy=True
    )

    print(
        "Embeddings created:",
        embeddings.shape
    )

    return chunks, embeddings


# ---------------------------------------------------------
# SEARCH DOCUMENTS
# ---------------------------------------------------------

def search_documents(
    query,
    chunks,
    embeddings,
    top_k=3
):

    if not chunks or embeddings is None:

        return []

    # Create embedding for user query
    query_embedding = embedding_model.encode(
        [query],
        convert_to_numpy=True
    )

    # Calculate similarity
    similarities = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    # Get highest similarity indexes
    top_indices = np.argsort(
        similarities
    )[::-1][:top_k]

    results = []

    for index in top_indices:

        results.append(
            {
                "filename": chunks[index]["filename"],
                "text": chunks[index]["text"],
                "score": float(
                    similarities[index]
                )
            }
        )

    return results