import requests
from bs4 import BeautifulSoup

# web link of the climate change publications
url = 'https://www.theccc.org.uk/publications/'


def create_web_reader(url):
    """
    Gets contents of a given website

    Parameters:
    url -- type is string

    Returns:
    html_content -- a string of the text inside the content    
    """
    read = requests.get(url)
    html_content = read.content
    return html_content

def all_report_links(url):
    """
    Fetches all pdfs available in a given web link

    Parameters:
    url -- type is string

    Returns:
    list_of_links -- a list of links that holds pdfs
    """
    html_content = create_web_reader(url)
    soup = BeautifulSoup(html_content, "html.parser")
    list_of_links = []
    """
    Finds all the a tags within the html code specific to
    class name of 'post-title__link' as that goes to the page 
    """
    links = soup.find_all('a', {'class': 'post-tile__link'})
    """
    Loops through all the urls given
    """
    for link in links:
        # 'href' holds the pdf url link
        temp = link.get("href")
        list_of_links.append(temp)
    return list_of_links

"""
Gets all the pages of the reports the website provides
returns:
list_of_links -- a list containing strings
"""
def get_report_links():
    list_of_links = []
    # loops 34 times due to 34 pages in its pagination
    for i in range(1,34):
        list_of_links.append(f'https://www.theccc.org.uk/publications/page/{i}/?topic&type=0-report')
    return list_of_links

# There for debugging purposes
print(len(get_report_links()))

"""
gets pdf from a given web page
parameters:
 - url --> type str
returns:
 - link --> type str
"""
def get_pdf(url):
    html_content = create_web_reader(url)
    soup = BeautifulSoup(html_content,"html.parser")
    # gets all the a tags from the html code of the page
    a_tags = soup.find_all('a')
    for a_tag in a_tags:
        pdf_link = a_tag.get('href')
        if '.pdf' in pdf_link:
            return pdf_link

"""
Puts together the methods above and returns
a list of pdfs

returns:
 - pdf_links --> a list containing items of type string
"""
def put_together():
    list_of_links = get_report_links()
    pdf_links = []
    for link in list_of_links:
        # Gets all report web links
        temp_list = all_report_links(link)
        for important_link in temp_list:
            # fetches pdf link from a certain report page
            pdf = get_pdf(important_link)
            if pdf != None:
                pdf_links.append(pdf)
    return pdf_links

"""
Puts all the pdf links into a text file
parameters:
    - pdf_list --> a list containing items of 
                    type string 
"""
def put_pdfs_in_file(pdf_list):
    with open('pdf_list.txt', 'w') as f:
        for pdf in pdf_list:
            if pdf != '.pdf':
                f.write(pdf)
                f.write('\n')


# main function that calls functions above
def main():
    pdf_links = put_together()
    put_pdfs_in_file(pdf_links)
    print(len(pdf_links))


main()

