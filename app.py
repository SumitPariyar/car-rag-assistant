import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever   # Import retriever from vector.py

# Load local Ollama LLM
model = OllamaLLM(model="llama3.2")

# Define the prompt template
template = """
You are an assistant for question-answering tasks.
Use the following context to answer the question.
If the answer is not in the context, say "I don’t know."

Context: {context}

Question: {question}
Answer:
"""
prompt = ChatPromptTemplate.from_template(template)

# Build the chain
chain = prompt | model

# ---------------- Streamlit UI ---------------- #
st.set_page_config(page_title="Car RAG Assistant", layout="wide")
st.title("🚗 Car RAG Assistant")
st.write("Ask me anything about the car dataset!")

# Input box for user
question = st.text_input("Enter your question:", placeholder="e.g. List cars between 10-11 lakhs")

if question:
    with st.spinner("Thinking..."):
        docs = retriever.invoke(question)  # fetch context
        result = chain.invoke({"context": docs, "question": question})

    # Show results
    st.subheader("Answer:")
    st.write(result)

    # Optionally show retrieved context
    with st.expander("See retrieved context"):
        for doc in docs:
            st.write(doc.page_content)
