import requests
from bs4 import BeautifulSoup
from utils import generate_regex

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
    regex_exp = generate_regex()

    for site in reuters_sites:
        r = requests.get(site)
        soup = BeautifulSoup(r.content, "lxml")
        headlines = soup.find_all("a", class_="media-story-card__heading__eqhp9")
        for news in headlines:
            unique_link = str(news["href"])
            result = regex_exp.match(unique_link)
            if result:
                reuters_headlines.append(news.contents[0].strip() + ".")
                reuters_links.append("reuters.com" + unique_link)
            else:
                continue
    return reuters_headlines, reuters_links