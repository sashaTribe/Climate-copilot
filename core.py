
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
    chat_history = []
    print("Hi and welcome to the climate change chatbot!!!")
    while True:
        user_input = input("Welcome! Ask me anything about Climate Change, or type 'quit' if you want to exit: ")
        if user_input == 'quit':
            print("See you Soon!")
            break
        if user_input == '':
            print("Sorry that is an invalid input, please try again")
        response = qa({"question": user_input, "chat_history":chat_history})
        print(f"Response: {response.get('answer')}")
        chat_history.append((user_input,response['answer']))