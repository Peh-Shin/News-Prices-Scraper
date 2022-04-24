import requests
from bs4 import BeautifulSoup
from utils import generate_regex

def CNBC():
    cnbc_headlines = []
    cnbc_links = []

    r = requests.get("https://www.cnbc.com/world/?region=world")
    soup = BeautifulSoup(r.content, "lxml")

    articles = soup.find_all("div", class_="FeaturedNewsHero-container")
    regex_exp = generate_regex()

    for article in articles:
        headlines = article.find_all("a")
        for headline in headlines:
            if headline.text != "":
                unique_link = str(headline["href"]).split(".", 1)[1]
                result = regex_exp.match(unique_link)
                if result:
                    cnbc_headlines.append(headline.text.strip() + ".")
                    cnbc_links.append(unique_link)
                else:
                    continue
    return cnbc_headlines, cnbc_links
