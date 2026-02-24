import os
from langchain_groq import ChatGroq

def get_llm():
    model_name = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

    return ChatGroq(
        model=model_name,
        temperature=0
    )