from rag import build_knowledge_base, search_documents
from granite_service import ask_granite


# Build knowledge base when the service starts
chunks, embeddings = build_knowledge_base()


def ask_rag(question):

    if not chunks:

        return (
            "No climate documents are currently available.",
            []
        )


    # Search knowledge base
    results = search_documents(
        question,
        chunks,
        embeddings,
        top_k=3
    )


    # Prepare retrieved information
    context_parts = []

    for result in results:

        context_parts.append(
            f"Source: {result['filename']}\n"
            f"{result['text']}"
        )


    context = "\n\n".join(
        context_parts
    )


    # Send retrieved context to Granite
    prompt = f"""
You are ClimateGuard AI.

Answer the user's question using the
provided reference information.

REFERENCE INFORMATION:
{context}

USER QUESTION:
{question}

Instructions:

- Use the reference information as the main source.
- Do not invent information that is not supported by it.
- If the answer is not available in the reference
  information, clearly say that the provided documents
  do not contain enough information.
- Use simple English.
- Mention the source file when useful.

ANSWER:
"""


    answer = ask_granite(
        prompt,
        max_new_tokens=300,
        temperature=0.2
    )


    return answer, results