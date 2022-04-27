import requests
from bs4 import BeautifulSoup


def get_futures():
    r = requests.get("https://www.marketwatch.com/investing/future/sp%20500%20futures")
    soup = BeautifulSoup(r.content, "lxml")

    futures = soup.find_all("div", class_="intraday__data")
    for future in futures:
        future_index = future.find("span", class_="value")
        if future_index == None:
            future_index = future.find("bg-quote", class_="value")
        future_change = future.find("span", class_="change--percent--q")
    return future_index.text, future_change.text


