from bs4 import BeautifulSoup
import requests
#from pyPDF2 import PdfFileReader

url = "https://www.theccc.org.uk/publications/"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
pdf_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.pdf')]

for pdf_link in pdf_links:
    pdf_url = url + pdf_link if not pdf_link.startswith('http') else pdf_link
    pdf_response = requests.get(pdf_url)
    with open(pdf_link.split("/")[-1], 'wb') as pdf_file:
        print("Writing to file....")
        pdf_file.write(pdf_response.content)

print("All files downloaded")

