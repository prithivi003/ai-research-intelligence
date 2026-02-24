# 🧠 AI Research Intelligence Platform

An AI-powered Research Assistant built using Retrieval-Augmented Generation (RAG) architecture.  
The platform enables users to interact with research papers through semantic search, structured summaries, and intelligent question answering.

---

## 🚀 Features

### 🔹 1. Global AI Research Chatbot
- Persistent vector database of AI research papers
- Semantic retrieval using FAISS
- Grounded answer generation via LLM
- Source citation display

### 🔹 2. My Paper Assistant
- Upload any research paper (PDF)
- Automatic chunking and embedding
- Session-based isolated vector database
- Ask contextual questions about the paper

### 🔹 3. Structured Summary Generator
- Generates academic-style structured summaries:
  - Problem Statement
  - Background / Motivation
  - Proposed Method
  - Experimental Setup
  - Results
  - Key Contributions
  - Limitations
  - Future Work

### 🔹 4. Dual RAG Architecture
- Persistent Global Knowledge Base
- Dynamic Session-Based Knowledge Base
- Clean isolation between document scopes

---

## 🏗️ Architecture

### 🔹 Indexing Phase (Offline)
1. Load PDFs
2. Chunk documents
3. Generate embeddings
4. Store vectors in FAISS database

### 🔹 Query Phase (Online)
1. Retrieve top-k relevant chunks
2. Send context + question to LLM
3. Generate grounded response
4. Display citations

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI
- **LangChain** – RAG orchestration
- **FAISS** – Vector database
- **Groq API (Llama 3.1)** – Large Language Model
- **Prompt Engineering**
- **Retrieval-Augmented Generation (RAG)**

