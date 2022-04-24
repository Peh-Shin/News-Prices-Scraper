import requests
from bs4 import BeautifulSoup


def get_futures():
    r = requests.get("https://www.marketwatch.com/investing/future/sp%20500%20futures")
    soup = BeautifulSoup(r.content, "lxml")

    futures = soup.find_all("div", class_="intraday__data")
    for future in futures:
        future_index = future.find("span", class_="value").text
        future_change = future.find("span", class_="change--percent--q").text
    return future_index, future_change

