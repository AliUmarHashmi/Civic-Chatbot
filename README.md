# Civic Issues RAG Chatbot

A domain-specific conversational AI chatbot for civic issue resolution, built using a Retrieval-Augmented Generation (RAG) pipeline.

## Features
- Ask questions related to civic issues and get context-aware answers
- RAG pipeline using FAISS vector store for semantic document retrieval
- Sentence-transformers for embedding generation
- Groq LLM for fast, accurate response synthesis
- Flask REST API backend with real-time query processing

## Tech Stack
- **Backend:** Flask, LangChain, FAISS, Sentence-Transformers
- **LLM:** Groq API
- **Embeddings:** HuggingFace Sentence-Transformers
- **Vector Store:** FAISS

## Setup

1. Clone the repo
2. Install dependencies:

pip install -r requirements.txt

3. Create a `.env` file:

GROQ_API_KEY=your_key_here

4. Run the app:

python app.py

## Project Structure

- app.py — Flask app entry point
- config.py — Configuration and environment variables
- rag/ — RAG pipeline logic
- data/ — Civic issues knowledge base
- templates/ — HTML frontend templates
- frontend/ — Frontend assets