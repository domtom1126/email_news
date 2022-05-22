import requests
from bs4 import BeautifulSoup

def getNews(): 
    URL = "https://news.ycombinator.com/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('a', class_='titlelink', href=True)
    # returns a list of all the links on the page on serpate lines 
    for link in results:
        link_list = [link.get('href')]
        return link_list[:10]
    

getNews()