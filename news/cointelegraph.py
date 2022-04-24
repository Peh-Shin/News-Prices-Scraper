import requests
import cloudscraper
from bs4 import BeautifulSoup


def cointelegraph():
    cointelegraph_headlines = []
    cointelegraph_links = []

    scraper = cloudscraper.create_scraper()
    r = scraper.get("https://cointelegraph.com/")
    soup = BeautifulSoup(r.content, "lxml")

    articles = soup.find_all("li", class_="posts-listing__item")
    for article in articles:
        label = article.find("span", class_="post-card__badge")
        if label:
            if (
                label.text.strip() == "News"
                or label.text.strip() == "Market News"
                or label.text.strip() == "Breaking news"
            ):
                links = article.find_all("a", class_="post-card__title-link")
                titles = article.find_all("span", class_="post-card__title")
                for title in titles:
                    if title.text != "":
                        cointelegraph_headlines.append(title.text.strip() + ".")
                for link in links:
                    cointelegraph_links.append("cointelegraph.com" + str(link["href"]))
    return cointelegraph_headlines, cointelegraph_links


