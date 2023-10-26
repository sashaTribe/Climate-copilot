
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone 
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import pinecone
import os

import keyboard
import sys

if os.path.exists('env.py'):
    import env


def run_llm(pinecone_env):
    pinecone.init(api_key=os.environ.get("PINECONE_SECRET_KEY"),
              environment=os.environ.get("PINECONE_ENVIRONMENT_REGION"))
    embedding = OpenAIEmbeddings(openai_key = os.environ.get("OPENAI_API_KEY"))
    doc_search = Pinecone.from_existing_index(
        index_name = 'climate-change',
        embedding = embedding
    )
    chat_model = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    qa = ConversationalRetrievalChain.from_llm(llm = chat_model, 
                                            retriever=doc_search.as_retriever())
    chat_log = []
    print("Hi and welcome to the climate change chatbot!!!")
    while True:
        user_input = input("Welcome! Ask me anything about Climate Change, or press 'Esc' if you want to exit: ")
        if keyboard.is_pressed('Esc'):
            print("See you Soon!")
            break
        response = qa({"question": user_input, "chat_history":chat_log})
        print(f"Response: {response.get('answer')}")
        chat_log.append((user_input,response))