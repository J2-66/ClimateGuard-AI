from rag import build_knowledge_base, search_documents


print("=" * 60)
print("       CLIMATEGUARD AI - RAG TEST")
print("=" * 60)


# ---------------------------------------------------------
# BUILD KNOWLEDGE BASE
# ---------------------------------------------------------

print("\nBuilding knowledge base...")

chunks, embeddings = build_knowledge_base()


print("\nNumber of chunks:", len(chunks))


# ---------------------------------------------------------
# CHECK DOCUMENTS
# ---------------------------------------------------------

if not chunks:

    print("\n❌ No documents found.")

    print(
        "\nPlease check the documents folder."
    )

    exit()


print(
    "Embeddings shape:",
    embeddings.shape
)


# ---------------------------------------------------------
# SEARCH
# ---------------------------------------------------------

print("\nSearching documents...")


query = "What should people do during flooding?"


results = search_documents(
    query,
    chunks,
    embeddings,
    top_k=3
)


# ---------------------------------------------------------
# DISPLAY RESULTS
# ---------------------------------------------------------

print("\nTop results:")
print("-" * 60)


for i, result in enumerate(
    results,
    1
):

    print(f"\nResult {i}")

    print(
        "File:",
        result["filename"]
    )

    print(
        "Similarity:",
        round(
            result["score"],
            4
        )
    )

    print("Text:")

    print(result["text"])


print(
    "\n" + "=" * 60
)

print(
    "✅ RAG RETRIEVAL TEST COMPLETE"
)

print(
    "=" * 60
)