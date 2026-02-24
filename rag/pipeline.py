def generate_answer(llm, query, retrieved_docs):
    # If no relevant docs found
    if not retrieved_docs:
        return "I don't know based on the provided research papers."

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
You are an AI research assistant.

Answer ONLY using the provided context.
If the context does not contain relevant information,
respond strictly with:
"I don't know based on the provided research papers."

Do not use outside knowledge.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)
    return response.content