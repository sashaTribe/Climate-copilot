import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
url = 'https://www.theccc.org.uk/publications/'
import csv

def create_web_reader(url):
    read = requests.get(url)
    html_content = read.content
    return html_content

def all_report_links(url):
    html_content = create_web_reader(url)
    soup = BeautifulSoup(html_content, "html.parser")
    list_of_links = []
    links = soup.find_all('a', {'class': 'post-tile__link'})
    for link in links:
        temp = link.get("href")
        list_of_links.append(temp)
    return list_of_links
#list = all_report_links(url)
#print(list[0])

def get_report_links():
    list_of_links = []
    for i in range(1,34):
        list_of_links.append(f'https://www.theccc.org.uk/publications/page/{i}/?topic&type=0-report')
    return list_of_links

print(len(get_report_links()))
"""
lst = []
for link in all_report_links(url):
    print(get_report_link(link))
    print('\n')
"""


def get_pdf(url):
    html_content = create_web_reader(url)
    soup = BeautifulSoup(html_content,"html.parser")
    a_tags = soup.find_all('a')
    for a_tag in a_tags:
        link = a_tag.get('href')
        if '.pdf' in link:
            return link

def put_together():
    list_of_links = get_report_links()
    pdf_links = []
    for link in list_of_links:
        temp_list = all_report_links(link)
        for final_link in temp_list:
            pdf = get_pdf(final_link)
            #print(pdf)
            if pdf != None:
                pdf_links.append(pdf)
    return pdf_links
"""
 test_list, test_list_two = put_together(url)
#my_list = [x for x in test_list if x != None]
my_list_two = [x for x in test_list_two if x != None]
#print(len(my_list))
print(len(my_list_two))
print(my_list_two[0])
 """   


def put_pdfs_in_file(pdf_list):
    with open('pdf_list.txt', 'w') as f:
        for pdf in pdf_list:
            if pdf != '.pdf':
                f.write(pdf)
                f.write('\n')


def main():
    pdf_links = put_together()
    put_pdfs_in_file(pdf_links)
    print(len(pdf_links))


main()

