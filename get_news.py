import requests
from bs4 import BeautifulSoup

def getNews(): 
    URL = "https://news.ycombinator.com/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('a', class_='titlelink', href=True)

    return results
