import requests
from bs4 import BeautifulSoup


def CNBC():
    cnbc_headlines = []
    cnbc_links = []

    r = requests.get("https://www.cnbc.com/world/?region=world")
    soup = BeautifulSoup(r.content, "lxml")

    articles = soup.find_all("div", class_="FeaturedNewsHero-container")
    for article in articles:
        headlines = article.find_all("a")
        for headline in headlines:
            if headline.text != "":
                cnbc_headlines.append(headline.text.strip() + ".")
                cnbc_links.append(str(headline["href"]).split(".", 1)[1])

    return cnbc_headlines, cnbc_links
