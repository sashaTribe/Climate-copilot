import requests
import bs4
import csv
import PyPDF2
import io 

def extract_text(pdf_link):
    response = requests.get(pdf_link)
    f = io.BytesIO(response.content)
    reader = PyPDF2.PdfReader(f)
    
    print(reader.pages[2].extract_text().split('\n'))

extract_text("https://www.theccc.org.uk/wp-content/uploads/2023/09/230925-PF-MN-ZEV-Mandate-Response.pdf")