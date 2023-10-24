import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
url = 'https://www.theccc.org.uk/publications/'
import csv


def get_tag_a(url):
    read = requests.get(url)
    html_content = read.content
    soup = BeautifulSoup(html_content, "html.parser")
    list_of_links = []
    a = soup.find_all('a')
    for link in a:
        list_of_links.append((link.get('href')))
    return list_of_links


def get_pdf(pdf):

    read = requests.get(url)
    html_content = read.content
    soup = BeautifulSoup(html_content, "html.parser")
    d = soup.find_all('div')
    a = soup.find_all('a')
    list_of_pdf = set()
    for link in a:
        #print("links: ", link.get('href'))
        #print("\n")
        
        # converting the extension from .html to .pdf
        pdf_link = (link.get('href')[:-5]) + ".pdf"
        
        # converted to .pdf
        print("converted pdf links: ", pdf_link)
        print("\n")
        
        # added all the pdf links to set
        list_of_pdf.add(pdf_link)
    return list_of_pdf


    
def put_pdfs_in_file(pdf_list):
    with open('pdf_list.txt', 'w') as f:
        for pdf in pdf_list:
            if pdf != '.pdf':
                f.write(pdf)
                f.write('\n')
        


def main():
    list_of_links = get_tag_a('https://www.theccc.org.uk/publications/')
    for link in list_of_links:
        temp_list = (get_pdf(link))
        put_pdfs_in_file(temp_list)

main()

