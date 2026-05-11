from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import OllamaEmbeddings

from langchain_chroma import Chroma


loader = TextLoader("app/rag/medical_data.txt")

documents = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)


embedding = OllamaEmbeddings(
    model="llama3"
)


vectorstore = Chroma.from_documents(
    docs,
    embedding,
    persist_directory="chroma_db"
)

print("Vector DB Created")