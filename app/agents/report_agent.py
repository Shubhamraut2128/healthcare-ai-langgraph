from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3"
)


def report_agent(state):

    disease = state["disease"]

    rag_data = state["rag_response"]

    prompt = f"""
    Disease: {disease}

    Medical Information:
    {rag_data}

    Create simple medical summary.
    """

    response = llm.invoke(prompt)

    return {
        "final_report": response.content
    }