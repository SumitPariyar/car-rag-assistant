🚗 Car RAG Assistant

Car RAG Assistant is an AI-powered question-answering system built on top of a car dataset. Using Retrieval-Augmented Generation (RAG), the app allows users to ask natural language questions about car listings and get precise, context-aware answers.

This project combines the power of LangChain, ChromaDB, and Ollama LLMs with an easy-to-use Streamlit web interface. It demonstrates how large language models can be integrated with structured datasets to make information retrieval seamless and intelligent.

✨ Features

📊 Car Dataset Integration → Query car details like name, year, price, fuel type, transmission, and more.

🔍 Semantic Search with ChromaDB → Retrieves the most relevant records using vector embeddings.

🧠 Local LLM with Ollama → Generates natural, human-like responses from the retrieved context.

💻 Two Interfaces:

CLI-based Q&A (terminal mode)

Streamlit Web App for interactive exploration

⚡ Fast & Lightweight → Runs locally without cloud dependencies.

🛠️ Tech Stack

Python (pandas, streamlit)

LangChain (core framework for RAG)

ChromaDB (vector database)

Ollama (local LLM & embeddings)

Streamlit (web interface)

🚀 Getting Started

Clone the repository:

git clone https://github.com/YourUsername/car-rag-assistant.git
cd car-rag-assistant


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

📂 Project Structure
car-rag-assistant/
│── app.py              # Streamlit web app
│── vector.py           # Vector store creation & retriever
│── main.py             # CLI-based interface
│── requirements.txt    # Python dependencies
│── car_data.csv        # Car dataset (sample)
│── chroma_langchain_db # Persisted Chroma database
│── README.md           # Project documentation

💡 Example Usage

Query:

"List cars between 5 and 6 lakhs with manual transmission"

Answer:

The dataset shows cars such as Maruti Swift (2015, ₹5.3L, Petrol, Manual) and Hyundai i20 (2016, ₹5.8L, Petrol, Manual).

📌 Future Improvements

Add data visualizations in Streamlit (price trends, fuel distribution).

Expand dataset to include more attributes.

Deploy using Docker for cloud portability.

👨‍💻 Author

Sumit Pariyar
📧 sumitpariyar1001@gmail.com
