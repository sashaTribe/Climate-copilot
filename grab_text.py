import requests
import bs4
import csv
import PyPDF2
import io 

def extract_text(pdf_link):
    response = requests.get(pdf_link)
    f = io.BytesIO(response.content)
    reader = PyPDF2.PdfReader(f)
    num_pages = len(reader.pages)
    for page_number in range(num_pages):
        page = reader.pages[page_number]
        page_text = page.extract_text()
        print(f"Page {page_number + 1}:\n{page_text}\n")

extract_text("https://www.theccc.org.uk/wp-content/uploads/2021/10/Independent-Assessment-of-the-UK-Net-Zero-Strategy-CCC.pdf")