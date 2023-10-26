import requests
import os
path = 'pdfs/'


"""
Downloads content from pdf's web link to a 
pdf file.
Parameters:
- pdf --> type str, the pdf url link
- index --> reference number for the file name
"""
def download_link(pdf,index):
    response = requests.get(pdf)
    # Makes sure that web access is successful
    if response.status_code == 200:
        # file name the contents will be downloaded to
        file_name = f'downloaded_file{index}.pdf'
        # combines file name to path for future processes
        file_path = os.path.join(path,file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print('PDF file downloaded successfully.')
    else:
        print(f'Failed to download the PDF. Status code: {response.status_code}')

# runs the above code for every pdf in the given pdf file
# Parameters:
# - file --> type str 
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
    


download_all_links('pdf_list.txt')

