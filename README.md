**PDF Question Answering Chatbot**
**Project Overview**

This project is a PDF Question Answering Chatbot built using Streamlit, LangChain, FAISS, and Ollama.
It allows users to:
1.Upload a PDF file
2.Ask questions about the PDF
3.Get accurate answers based only on the uploaded document

**How It Works:**

1.User uploads a PDF file.
2.The PDF is read and split into small text chunks.
3.These chunks are converted into vector embeddings.
4.The vectors are stored in a FAISS vector database.
5.When the user asks a question:
   .The system finds the most relevant text from the PDF.
   .The LLM (phi3 model via Ollama) generates an answer.
6.The answer is displayed on the screen.

**Technologies Used**

🐍 Python
🌐 Streamlit (for web app UI)
🔗 LangChain (for chaining LLM + retrieval)
🤗 HuggingFace Embeddings
📚 FAISS (Vector Database)
🦙 Ollama (LLM - phi3 model)
📄 PyMuPDF (for reading PDF files)

**Installation**

1️⃣ **Clone the Repository**

git clone https://github.com/your-username/PDF-Question-Answering-Chatbot.git
cd PDF-Question-Answering-Chatbot

2️⃣ **Install Required Packages**

pip install -r requirements.txt
If you don’t have a requirements.txt, install manually:
pip install streamlit langchain langchain-community langchain-huggingface faiss-cpu pymupdf ollama

**Install Ollama and Model**

Download and install Ollama from:
https://ollama.com
Pull the llama2 model:
ollama pull llama2

▶️ **Run the Application**

streamlit run app.py

The app will open in your browser.

**📌 Project Structure**

PDF-Question-Answering-Chatbot/
│
├── app.py
├── README.md
└── requirements.txt

**💡 Features**

✔ Upload any PDF
✔ Ask questions about the PDF
✔ Fast semantic search using FAISS
✔ Uses local LLM (No OpenAI API required)
✔ Simple and beginner-friendly interface


📷 **Example Usage**

Upload a Budget PDF.
Ask:
"What is the total expenditure?"
"What is the allocation for education?"
Get instant answers from the document.

**🎯 Future Improvements**

Add chat history
Support multiple PDFs
Add source references in answers
Deploy on cloud (Streamlit Cloud)


**👨‍💻 Author**

**THOTA VIJAYASIMHA**
B.Tech - Electronics and Communication Engineering
Interested in Gen AI, AI and Machine Learning

**GitHub**: https://github.com/Vijaya-Simha77

⭐ If You Like This Project

Give it a ⭐ on GitHub!

