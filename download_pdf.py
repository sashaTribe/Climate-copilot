import requests
import os
path = 'pdfs/'

def download_all_links(file):
    list_of_pdfs = []
    with open(file, 'r') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            modified_line = line.replace("\n", "")
            download_link(str(modified_line), i)
            i+=1
    print("Files downloaded")
    

def download_link(pdf,index):
    response = requests.get(pdf)

    if response.status_code == 200:
        file_name = f'downloaded_file{index}.pdf'
        file_path = os.path.join(path,file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print('PDF file downloaded successfully.')
    else:
        print(f'Failed to download the PDF. Status code: {response.status_code}')

download_all_links('pdf_list.txt')

