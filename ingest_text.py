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

# initialises pinecone client 
pinecone.init(api_key=os.environ.get("PINECONE_SECRET_KEY"),
              environment=os.environ.get("PINECONE_ENVIRONMENT_REGION"))
active_indexes = pinecone.list_indexes()
# gets index of the client you are submitting embeddings to
index = pinecone.Index('climate-change')

"""
reads all the pdf links from the given file

parameters:
- pdf_list_file --> the file name of all the pdf links stored

return:
- pdf_link_list --> a list containing string objects (pdf web links)
"""
def get_all_pdfs(pdf_list_file):
    pdf_link_list = []
    with open(pdf_list_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            pdf_link_list.append(line)
    return pdf_link_list


"""
Extracts text data from the given pdf 

parameters:
- pdf_path --> type str containing the path of the pdf

returns:
- text --> a big string of text 
"""
def extract_text_from_pdf(pdf_path):
    text = ""
    with PyPDF2.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

"""
loads and splits data using Langchain
parameters:
- pdf --> str type
- pages --> a list of string objects
"""
def load_pdf(pdf):
    print(pdf)
    loader = PyPDFLoader(pdf)
    pages = loader.load_and_split()
    return pages

"""
extracts text from given pages
- page --> list of string objects
"""
def extract_text(page):
    
    # splits text into 250 characters with 50 character overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 250,
        chunk_overlap = 50,
        separators =["\n\n", "\n", "",""]
    )

    # splits the pages up into smaller texts
    document = text_splitter.split_documents(page)

    # creates embedding tool from openai 
    embedding = OpenAIEmbeddings(open_ai_key = os.environ.get("OPEN_AI_KEY"))

    # processes the documents, creating embeddings for each document and upload them to
    # pinecone client called 'climate-change'
    Pinecone.from_documents(documents = document, embedding=embedding, index_name='climate-change')
    print("Successful upload")

# This calls all the functions above
def upload_pdf():
    path = 'pdfs/'
    #pdf_files = [f for f in os.listdir(path) if f.endswith('.pdf')]
    pdf_files = []
    for file in os.listdir(path):
        # joining the path and file together 
        if os.path.isfile(os.path.join(path, file)):
            pdf_files.append(os.path.join(path, file))
    print(len(pdf_files))
    print(pdf_files[0])
    for pdf in pdf_files:
        pages = load_pdf(pdf)
        extract_text(pages)

if __name__ == "__main__":
    upload_pdf()