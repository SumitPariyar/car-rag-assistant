
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma   # Chroma is from langchain_chroma
from langchain_core.documents import Document
import os
import pandas as pd

# Load your CSV
df = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv")

# Create embeddings instance
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Vector DB path
db_location = "./chroma_langchain_db"

# Check if DB already exists
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        # Convert row into a readable string
        content = (
            f"Car Name: {row['name']}, "
            f"Year: {row['year']}, "
            f"Selling Price: {row['selling_price']}, "
            f"Km Driven: {row['km_driven']}, "
            f"Fuel: {row['fuel']}, "
            f"Seller Type: {row['seller_type']}, "
            f"Transmission: {row['transmission']}, "
            f"Owner: {row['owner']}"
        )

        # Make a Document object
        document = Document(page_content=content, metadata={"row_id": i})

        documents.append(document)
        ids.append(str(i))  

# ✅ Fix: use embedding_function instead of embeddings_function
vector_store = Chroma(
    collection_name="car_details",
    embedding_function=embeddings,
    persist_directory=db_location
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)


