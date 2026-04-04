RAG_system1

Small RAG demo that loads a PDF, chunks it, generates embeddings via Ollama, and stores them in a vector store.

Flow:
pdf book -> .txt -> chunks -> embedding(ollama embedding) -> vector DB(chroma DB)

Commands for libraries installation:

pip install langchain-community pypdf

pip install PyPDF2
