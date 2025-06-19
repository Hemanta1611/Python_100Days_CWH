"""
Scanario: Web Scraping
Web Scraping often involves making numerous network requests to different web pages to extract data from them.
These tasks are I/O bound because they sped a lot of time waiting for the web page to load and waiting for responses from servers.
Multi-threading can significantly improve the performance of web scraping tasks by allowing multiple web pages to be fetched concurrently.
"""

import requests
from bs4 import BeautifulSoup
import threading
import time

url1 = "https://python.langchain.com/v0.2/docs/introduction/getting_started.html"
url2 = "https://python.langchain.com/v0.2/docs/concepts/"
url3 = "https://python.langchain.com/v0.2/docs/tutorials/"

urls = [url1, url2, url3]
threads = []
t = time.time()

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

for url in urls:
    fetch_content(url)

finished_time = time.time() - t
print("finished time for single thread: ", finished_time, "\n")
t = time.time()


for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    
print("All web pages have been fetched.")
finished_time = time.time() - t
print("finished time for multi-threading: ", finished_time)