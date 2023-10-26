# Climate-Copilot
An LLM that processes a corpus of climate change documents to the pinecone server, including a prompt for users to make queries relating to climate change environment. 
This project saves the user the effort to go through all the reports to find information of a particular subject by providing a prompt for them to type in their query and the LLM produces an answer.
### The link that holds all of the reports:
https://www.theccc.org.uk/publications/

## Technologies I have used:
- Langchain: 
    - I have used Langchain to tokenize and make embeddings of the text that is being processed 
    - It holds sentimental analysis
- Pinecone
    - Pinecone holds all the vectors of the processed PDFs, it is easy to grab data from after the user's query
- requests
    - Important for web scraping
- OpenAI
    - a tool that powers my LLM model
- BeautifulSoup
    - Makes it easier for me to find pdf links of a given website


## What has been challenging for me:
- Finding the best way to grab the text inside of the PDF reports
- Trying to get Streamlit to work however it has been unsuccessful with my computer as the technologies I use is incompatible to streamlit

## The Code Section

