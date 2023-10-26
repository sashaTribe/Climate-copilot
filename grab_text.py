import requests
import PyPDF2
import io 
import os
output_folder = "pdfs/"
import fitz
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


def load_pdf(pdf):
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


#text = load_pdf("https://www.theccc.org.uk/about/car.pdf")
#extract_text(text)




def load_pdfs_to_loader(pdf_list):
    list_of_pages = []

    for pdf in pdf_list:
        try:
            list_of_pages.append(load_pdf(pdf))
        except ValueError:
            pass
    print(len(list_of_pages))
    print(len(list_of_pages[0]))
    return list_of_pages


def main():
    list_of_pdf_links = get_all_pdfs('pdf_list.txt')
    list_of_pages = load_pdfs_to_loader(list_of_pdf_links)
    #page = load_pdf("https://www.theccc.org.uk/wp-content/uploads/2023/09/230925-PF-MN-ZEV-Mandate-Response.pdf")
    return len(list_of_pages)
    """
    faiss_index = FAISS.from_documents(page, OpenAIEmbeddings())
    docs = faiss_index.similarity_search("Climate? ", k=2)
    for doc in docs:
        print(str(doc.metadata["page"]) + ":", doc.page_content[:300])
    """
    

main()
#extract_text("https://www.theccc.org.uk/wp-content/uploads/2021/10/Independent-Assessment-of-the-UK-Net-Zero-Strategy-CCC.pdf")

if __name__ == "__main__":
    main()