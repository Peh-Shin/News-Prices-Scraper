from datetime import date, datetime

from news.reuters import reuters
from news.cnbc import CNBC
from news.coindesk import coindesk
from news.cointelegraph import cointelegraph
from news.theblockcrypto import theblock

from prices.BTC_ETH import BTC_ETH_prices
from prices.SPfutures import get_futures


def get_headlines():
    # TradFi News
    tradfi = list(zip(*reuters())) + list(zip(*CNBC()))
    # Crypto News
    crypto = (
        list(zip(*coindesk())) + list(zip(*cointelegraph())) + list(zip(*theblock()))
    )
    return tradfi, crypto


def get_prices_futures():
    return *BTC_ETH_prices(), get_futures()


def main():
    news_headlines = get_headlines()
    prices_futures = get_prices_futures()

    with open(f"news.txt", "w", encoding="utf-8") as f:
        f.write("Morning News\n")
        f.write(f'{date.today().strftime("%B %d, %Y")}\n')
        f.write(f'Singapore Time: {datetime.now().strftime("%H:%M")} am\n\n')
        f.write(f"BTC: {prices_futures[0][0]} ({prices_futures[0][1]})\n")
        f.write(f"ETH: {prices_futures[1][0]} ({prices_futures[1][1]})\n")
        f.write(f"S&P500 Futures: ${prices_futures[2][0]} ({prices_futures[2][1]})\n")

        f.write("\nTraditional Finance\n")
        for tradfinews in news_headlines[0]:
            f.write("   \u2022")
            f.write(f"   {tradfinews[0]}\n")
            f.write(f"{tradfinews[1]}\n")

        f.write("\nCrypto\n")
        for cryptonews in news_headlines[1]:
            f.write("   \u2022")
            f.write(f"   {cryptonews[0]}\n")
            f.write(f"{cryptonews[1]}\n")


if __name__ == "__main__":
    main()
