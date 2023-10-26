
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone 
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import pinecone
import os
import streamlit as st

if os.path.exists('env.py'):
    import env

st.write("Hello Sasha I am a computer")

def run_llm(query:str):
    pinecone.init(api_key=os.environ.get("PINECONE_SECRET_KEY"),
              environment=os.environ.get("PINECONE_ENVIRONMENT_REGION"))
    embedding = OpenAIEmbeddings(openai_key = os.environ.get("OPENAI_API_KEY"))
    doc_search = Pinecone.from_existing(
        index_name = 'climate-change',
        embedding = embedding
    )
    chat_model = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    qa = RetrievalQA.from_chain_type(chain_type="stuff", 
                                     llm = chat_model, 
                                     retriever=doc_search.as_retriever())
    return qa({"query":query})