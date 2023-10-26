import PyPDF2
import os
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pinecone
from langchain.vectorstores import Pinecone
if os.path.exists("env.py"):
    import env

pinecone.init(api_key=os.environ.get("PINECONE_SECRET_KEY"),
              environment=os.environ.get("PINECONE_ENVIRONMENT_REGION"))
active_indexes = pinecone.list_indexes()
index = pinecone.Index('climate-change')

def get_all_pdfs(pdf_list_file):
    pdf_link_list = []
    with open(pdf_list_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            pdf_link_list.append(line)
    return pdf_link_list



def extract_text_from_pdf(pdf_path):
    text = ""
    with PyPDF2.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def load_pdf(pdf):
    print(pdf)
    loader = PyPDFLoader(pdf)
    pages = loader.load_and_split()
    return pages

def extract_text(page):
    text = ""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 250,
        chunk_overlap = 50,
        separators =["\n\n", "\n", "",""]
    )
    document = text_splitter.split_documents(page)
    embedding = OpenAIEmbeddings(open_ai_key = os.environ.get("OPEN_AI_KEY"))
    Pinecone.from_documents(documents = document, embedding=embedding, index_name='climate-change')
    print("Successful upload")

def upload_pdf():
    path = 'pdfs/'
    #pdf_files = [f for f in os.listdir(path) if f.endswith('.pdf')]
    pdf_files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            pdf_files.append(os.path.join(path, file))
    print(len(pdf_files))
    print(pdf_files[0])
    for pdf in pdf_files:
        pages = load_pdf(pdf)
        extract_text(pages)

if __name__ == "__main__":
    upload_pdf()