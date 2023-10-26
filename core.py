
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone 
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import pinecone
import os

# Imports env file for api key access
if os.path.exists('env.py'):
    import env

"""
Creates an agent that answers user's query with a prompt on the terminal
Parameters:
- pinecone_env --> a string???
"""
def run_llm(pinecone_env):
    # initialises pinecone client 
    pinecone.init(api_key=os.environ.get("PINECONE_SECRET_KEY"),
              environment=os.environ.get("PINECONE_ENVIRONMENT_REGION"))
    
    # connects to openAI for embeddings
    embedding = OpenAIEmbeddings(openai_key = os.environ.get("OPENAI_API_KEY"))

    # sets up a search connecting to your pinecone index with use of embeddings 
    # created
    doc_search = Pinecone.from_existing_index(
        index_name = 'climate-change',
        embedding = embedding
    )
    # builds an LLM connecting to OpenAI
    chat_model = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))

    # sets up agent and prompt with the LLM and the searcher (doc_search) to retrieve information
    qa = ConversationalRetrievalChain.from_llm(llm = chat_model, 
                                            retriever=doc_search.as_retriever())
    chat_history = []
    print("Hi and welcome to the climate change chatbot!!!")
    # code below runs until user wants to quit from prompt
    while True:
        user_input = input("Welcome! Ask me anything about Climate Change, or type 'quit' if you want to exit: ")
        if user_input == 'quit':
            print("See you Soon!")
            break
        if user_input == '':
            print("Sorry that is an invalid input, please try again")
        # the answer gained from the query and chat history
        response = qa({"question": user_input, "chat_history":chat_history})
        # provides answer to user
        print(f"Response: {response.get('answer')}")
        # adds the query and answer to the log
        chat_history.append((user_input,response['answer']))