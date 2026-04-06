from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma

# -----------------------------
# STEP 1: Load PDF
# -----------------------------
file_path = r"C:\Users\rkjha\Downloads\RAG application-ref -insta_nilesh\Think-And-Grow-Rich_2011-06.pdf"

loader = PyPDFLoader(file_path)
docs = loader.load()

print(f"Total pages: {len(docs)}")

# -----------------------------
# STEP 2: Better Chunking
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,     # smaller chunks = better retrieval
    chunk_overlap=50,   # less repetition
    add_start_index=True
)

all_splits = text_splitter.split_documents(docs)

print(f"Total chunks: {len(all_splits)}")

# -----------------------------
# STEP 3: Embeddings
# -----------------------------
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# -----------------------------
# STEP 4: Vector DB
# -----------------------------
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db"
)

vector_store.add_documents(all_splits)

print("Documents stored in vector DB")

# -----------------------------
# STEP 5: Query
# -----------------------------
query = "burning desire as a driving force"

# Use MMR for diverse results
retrieved_docs = vector_store.max_marginal_relevance_search(query, k=5)

# -----------------------------
# STEP 6: Remove duplicate chunks
# -----------------------------
unique_texts = []
unique_docs = []

for doc in retrieved_docs:
    if doc.page_content not in unique_texts:
        unique_texts.append(doc.page_content)
        unique_docs.append(doc)

retrieved_docs = unique_docs[:3]

# -----------------------------
# STEP 7: Show retrieved chunks
# -----------------------------
print("\nTop retrieved chunks:\n")
for i, doc in enumerate(retrieved_docs):
    print(f"--- Chunk {i+1} ---")
    print(doc.page_content[:300])
    print()

# -----------------------------
# STEP 8: Build context
# -----------------------------
context = "\n\n".join([doc.page_content for doc in retrieved_docs])

# -----------------------------
# STEP 9: LLM
# -----------------------------
llm = ChatOllama(
    model="phi",   # fast + works without tool issues
    temperature=0
)

# -----------------------------
# STEP 10: Better Prompt
# -----------------------------
prompt = f"""
You are answering questions from a book.

Use ONLY the provided context.
If the answer is not clearly in the context, say "Not found in context".

Context:
{context}

Question:
{query}

Give a clear, specific, and concise answer.
"""

# -----------------------------
# STEP 11: Generate Answer
# -----------------------------
response = llm.invoke(prompt)

print("\n================ FINAL ANSWER ================\n")
print(response.content)