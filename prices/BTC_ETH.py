import requests
from bs4 import BeautifulSoup
from config import coindesk_html

def BTC_ETH_prices():
    soup = BeautifulSoup(coindesk_html, "lxml")
    coins = soup.find_all(
        "div", class_="price-navigationstyles__PricingItemWrapper-sc-1okl49q-0"
    )
    prices = []
    percent_change = []
    for coin in coins:
        if coin.a["href"] == "/price/bitcoin/" or coin.a["href"] == "/price/ethereum/":
            for index, element in enumerate(coin.div):
                if index % 2 == 0:
                    prices.append(element.text)
                else:
                    percent_change.append(element.text)
    return zip(prices, percent_change)


