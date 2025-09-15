from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever   # your retriever from vector.py

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

chain = prompt | model


while True:
    print("\n\n--------------------")
    question = input("Ask your question (q to quit):")
    print("\n\n")
    if question == "q":
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({"context": reviews, "question": question})
    print(result)


