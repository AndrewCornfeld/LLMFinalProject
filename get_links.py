import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()

def crawl(url, depth=2):
    if url in visited or depth == 0:
        return
    visited.add(url)
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a", href=True):
            next_url = urljoin(url, link["href"])
            if next_url.startswith("https://"):
                #print(next_url)
                crawl(next_url, depth - 1)
    except:
        pass

urls = [
    "https://virginia.edu/apply",
    "https://virginia.edu/alumni",
    "https://virginia.edu/facts",
    "https://virginia.edu/academics",
    "https://virginia.edu/life",
]
for url in urls:
    crawl(url)
print("\n".join(visited))
