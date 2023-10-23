from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import pinecone
from langchain.chat_models import ChatOpenAI

import pprint
import pinecone
import os


"""
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
"""

def grab_corpus(url):
    loader = AsyncChromiumLoader(url)
    html = loader.load()

    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["a"])
    docs_transformed[0].page_content[0:500]

grab_corpus("https://www.theccc.org.uk/publications/")