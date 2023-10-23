from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import pinecone
import pinecone
import os

if os.path.exists("env.py"):
    import env

pinecone.init(api_key=os.environ("PINECONE_SECRET_KEY"),
              environment=os.environ.get("PINECONE_ENVIRONMENT_REGION"))

