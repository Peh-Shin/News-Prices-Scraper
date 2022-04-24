import requests
from bs4 import BeautifulSoup


def reuters():
    reuters_headlines = []
    reuters_links = []

    reuters_sites = [
        "https://www.reuters.com/markets/",
        "https://www.reuters.com/markets/rates-bonds/",
        "https://www.reuters.com/markets/us/",
        "https://www.reuters.com/markets/stocks/",
        "https://www.reuters.com/markets/macromatters/",
    ]
    for site in reuters_sites:
        r = requests.get(site)
        soup = BeautifulSoup(r.content, "lxml")
        headlines = soup.find_all("a", class_="media-story-card__heading__eqhp9")
        for news in headlines:
            reuters_headlines.append(news.contents[0].strip() + ".")
            reuters_links.append("reuters.com" + str(news["href"]))
    return reuters_headlines, reuters_links


