import requests
from bs4 import BeautifulSoup
import cloudscraper

def theblock():
    theblock_headlines = []
    theblock_links = []

    scraper = cloudscraper.create_scraper()
    r = scraper.get("https://www.theblockcrypto.com/")
    soup = BeautifulSoup(r.content, "lxml")

    articles = soup.find_all("a", class_="theme color-outer-space")
    for article in articles:
        theblock_headlines.append(article.text.strip() + ".")
        theblock_links.append("www.theblockcrypto.com" + str(article["href"]))
    return theblock_headlines, theblock_links
