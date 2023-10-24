import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
url = 'https://www.theccc.org.uk/publications/'
import csv


def all_report_links(url):
    read = requests.get(url)
    html_content = read.content
    soup = BeautifulSoup(html_content, "html.parser")
    list_of_links = []
    links = soup.find_all('a', {'class': 'wp-block-button__link'})
    for link in links:
        temp = link.get("href")
        list_of_links.append(temp)
    return list_of_links

print(all_report_links(url))

def get_report_link(given_link):
    read = requests.get(given_link)
    html_content = read.content
    soup = BeautifulSoup(html_content, "html.parser")
    links = soup.find('a').get('href')
    links = soup.find_all('a', {'class': 'post-title__link'})
    list_of_links = []
    for link in links:
        temp = link.get("href")
        list_of_links.append(temp)
    return list_of_links

def get_pdf(url):

    read = requests.get(url)
    html_content = read.content
    soup = BeautifulSoup(html_content, "html.parser")
    link = soup.find_all('a', {'class': 'wp-block-button_link is-align-left'})
    return link


    
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

#main()

