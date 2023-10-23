from bs4 import BeautifulSoup
import requests

url = "https://www.theccc.org.uk/publications/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
i = 0

for link in links:
    if ('.pdf' in link.get('href', [])):
        i += 1
        print("Downloading File: ", i)

        response = requests.get(link.get('href'))
        pdf = open("pdf"+str(i)+".pdf",'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ",i," downloaded")

print("All files downloaded")