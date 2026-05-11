from langchain_chroma import Chroma

from langchain_ollama import OllamaEmbeddings


embedding = OllamaEmbeddings(
    model="llama3"
)


vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding
)


def rag_agent(state):

    disease = state["disease"]

    docs = vectorstore.similarity_search(disease)

    result = docs[0].page_content

    return {
        "rag_response": result
    }