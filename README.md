RAG-based PDF Question Answering System

Overview:
This project implements a Retrieval-Augmented Generation (RAG) pipeline to enable intelligent question answering over a PDF document.
The system reads a PDF, converts it into embeddings, stores them in a vector database, and retrieves relevant context to generate accurate answers using a local LLM.

How It Works:
1. Load PDF
Reads the PDF file using a document loader.
Converts it into structured text.
2. Text Chunking
Splits large text into smaller chunks.
Uses overlap to maintain context.
3. Embedding Generation
Converts text chunks into vector embeddings.
Uses a local embedding model.
4. Vector Database (ChromaDB)
Stores embeddings for efficient similarity search.
Enables fast retrieval of relevant chunks.
5. Similarity Search
Converts user query into embedding.
Retrieves top-k relevant chunks.
6. LLM Response Generation
Passes retrieved context + query to local LLM.
Generates accurate, context-aware answers.

Tech Stack:
Python
LangChain
Ollama (Local LLMs)
ChromaDB (Vector Database)

Project Structure:
RAG_system1/
│── main.py              # Main RAG pipeline
│── chroma_langchain_db/ # Vector database storage
│── README.md            # Project documentation

Setup & Installation:
1. Clone the repository
git clone https://github.com/pragjha/RAG_system1.git
cd RAG_system1
2. Install dependencies
pip install langchain langchain-community langchain-ollama langchain-chroma
3. Install and run Ollama
Download from: https://ollama.com
4. Pull required models
ollama pull nomic-embed-text
ollama pull phi

Run the Project:
python main.py

Example Query:
burning desire as a driving force
Output:
Retrieves relevant chunks from PDF
Generates answer using LLM
