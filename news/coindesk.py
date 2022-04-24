import requests
from bs4 import BeautifulSoup
from config import coindesk_html
from utils import generate_regex

def coindesk():
    coindesk_headlines = []
    coindesk_links = []

    soup = BeautifulSoup(coindesk_html, "lxml")
    crypto_news = soup.find_all(
        "div", class_="live-wirestyles__Body-sc-1ntysli-1 eEIZQY"
    )
    regex_exp = generate_regex()    
    for idea in crypto_news:
        crypto_titles = idea.find_all("a", class_="Box-sc-1hpkeeg-0 hdfPqS")
        for bar in crypto_titles:
            unique_link = str(bar["href"])
            result = regex_exp.match(unique_link)
            if result:
                if bar.text[:11] == "Market Wrap":
                    coindesk_headlines.insert(0, bar.text.strip() + ".")
                    coindesk_links.insert(0, "coindesk.com" + unique_link)
                else:
                    coindesk_headlines.append(bar.text.strip() + ".")
                    coindesk_links.append("coindesk.com" + unique_link)
            else:
                continue
        return coindesk_headlines, coindesk_links


