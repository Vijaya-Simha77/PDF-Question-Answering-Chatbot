import os
import streamlit as st
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA
from langchain_ollama import OllamaLLM

st.set_page_config(page_title="Budget Chatbot", layout="wide")
st.title("PDF Question Answering Chatbot")

uploaded_file = st.file_uploader("Upload Budget PDF", type="pdf")
#query = st.text_input("Ask your question")

if uploaded_file is not None and "vectorstore" not in st.session_state:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF Uploaded Successfully")

    loader = PyMuPDFLoader("temp.pdf")
    documents = loader.load()
    #print("Total Pages Loaded:", len(documents))

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    documents = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(documents, embeddings)
    st.session_state.vectorstore = vectorstore

    if os.path.exists("temp.pdf"):
        os.remove("temp.pdf")

if "vectorstore" in st.session_state:

    retriever = st.session_state.vectorstore.as_retriever()

    llm = OllamaLLM(
        model="phi3",  # mistral
        temperature=0.2
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )
    query=st.text_input("Ask a Question About your PDF")
    
    if query:
        response = qa_chain.invoke({"query": query})
        st.subheader("Answer:")
        st.write(response["result"])