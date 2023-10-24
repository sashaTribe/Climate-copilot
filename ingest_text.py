from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import pinecone
from langchain.chat_models import ChatOpenAI
from playwright.async_api import async_playwright
from langchain.chains import create_extraction_chain
from bs4 import BeautifulSoup
import pprint
import pinecone
import os

if os.path.exists("env.py"):
    import env
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
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613",openai_api_key=os.environ.get("OPEN_AI_KEY"))
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["a"])
    docs_transformed[0].page_content[0:500]

#grab_corpus("https://www.theccc.org.uk/publications/")

schema = {
    "Properties" : {
        "content" : {"type" : "string"},
    },
    "required": ["content"],
}
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
def extract(content: str, schema: dict):
    return create_extraction_chain(schema=schema, llm=llm).run(content)

def scrape_with_playwright(urls, schema):
    
    loader = AsyncChromiumLoader(urls)
    docs = loader.load()
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(docs,tags_to_extract=["a"])
    print("Extracting content with LLM")
    
    # Grab the first 1000 tokens of the site
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=1000, 
                                                                    chunk_overlap=0)
    splits = splitter.split_documents(docs_transformed)
    
    # Process the first split 
    extracted_content = extract(
        schema=schema, content=splits[0].page_content
    )
    pprint.pprint(extracted_content)
    return extracted_content

urls = ["https://www.theccc.org.uk/publications/"]
extracted_content = scrape_with_playwright(urls, schema=schema)