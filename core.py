
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone 
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import pinecone
import os
import streamlit as st
from streamlit_chat import message

# Imports env file for api key access
if os.path.exists('env.py'):
    import env

"""
Creates an agent that answers user's query with a prompt on the terminal
Parameters:
- pinecone_env --> the environment name
"""
def run_llm():
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
    chain = ConversationalRetrievalChain.from_llm(llm = chat_model, 
                                            retriever=doc_search.as_retriever())
    
    def conversational_chat(query):
        result = chain({"question": query, "chat_history": st.session_state['history']})
        st.session_state['history'].append((query, result["answer"]))
        return result["answer"]

    # Initialize chat history
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    # Initialize messages
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello ! Ask me about climate change 🤗"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey ! 👋"]

    st.title("Climate Change Chatbot")
    
    response_container = st.container()
    container = st.container()

    # User input form
    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input("Query:", placeholder="Ask a question about climate change", key='input')
            submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            output = conversational_chat(user_input)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    # Display chat history
    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="personas")
                message(st.session_state["generated"][i], key=str(i), avatar_style="icons")

    