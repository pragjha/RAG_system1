from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

file_path=r"C:\Users\rkjha\Downloads\RAG application-ref -insta_nilesh\Think-And-Grow-Rich_2011-06.pdf"
loader=PyPDFLoader(file_path)
docs=loader.load()

print(len(docs))
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)
    

all_splits=text_splitter.split_documents(docs)

print(all_splits[1])
print(len(all_splits))

