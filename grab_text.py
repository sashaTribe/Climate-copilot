import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Define the URL of the webpage containing the links to the PDFs
url = 'https://www.theccc.org.uk/publications/'

response = requests.get(url)
content = BeautifulSoup(response.text, 'html.parser')
all_urls = [content.find_all('a')]
i=0
for url in all_urls:
    new_content = BeautifulSoup(response.text, 'html.parser')
    inner_urls = [new_content.find_all('a')]
    for pdf_url in inner_urls:
        if ('.pdf' in pdf_url):
            i += 1
            print("Downloading file: ", i)
    
            # Get response object for link
            response = requests.get(pdf_url)
    
            # Write content in pdf file
            pdf = open("pdf"+str(i)+".pdf", 'wb')
            pdf.write(response.content)
            pdf.close()
            print("File ", i, " downloaded")
print("All files downloaded")

