from langchain.document_loaders import AsyncHtmlLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import pinecone
from langchain.chat_models import ChatOpenAI
from bs4 import BeautifulSoup
import pprint
import pinecone
import os

if os.path.exists("env.py"):
    import env

pinecone.init(api_key=os.environ("PINECONE_SECRET_KEY"),
              environment=os.environ.get("PINECONE_ENVIRONMENT_REGION"))

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
url = "https://www.theccc.org.uk/publications/"
loader = AsyncHtmlLoader(url)
docs = loader.load()


def grab_corpus(url,schema):
    loader = Async
