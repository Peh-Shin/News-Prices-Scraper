import os
import requests
from datetime import date, datetime, timedelta
from bs4 import BeautifulSoup
import cloudscraper
from selenium import webdriver

#Reuters 
sites = ['https://www.reuters.com/markets/', 'https://www.reuters.com/markets/rates-bonds/', 'https://www.reuters.com/markets/us/', 'https://www.reuters.com/markets/stocks/', 'https://www.reuters.com/markets/macromatters/', 'https://www.reuters.com/markets/us/']
for site in sites:
    r = requests.get(site)
    soup = BeautifulSoup(r.content, 'lxml')

    final_headlines = []
    final_links = []

    headlines = soup.find_all('a', class_ = "media-story-card__heading__eqhp9")
    for link in headlines:
        final_headlines.append(link.contents[0].strip()+'.')
        final_links.append('reuters.com' + str(link['href']))


#CNBC
r = requests.get("https://www.cnbc.com/world/?region=world") 
soup = BeautifulSoup(r.content, 'lxml')

finance_news = soup.find_all('div', class_= 'FeaturedNewsHero-container')
for fin in finance_news:
    the_titles = fin.find_all('a')
    for foo in the_titles:  
        if foo.text != '':
            final_headlines.append(foo.text.strip() +'.')
            final_links.append(str(foo['href']).split('.', 1)[1])

#Coindesk
url = 'https://www.coindesk.com/'
delay = 30

crypto_headlines = []
crypto_links = []

driver.get(url)
driver.implicitly_wait(delay)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
crypto_news = soup.find_all('div', class_= 'live-wirestyles__Body-sc-1ntysli-1 eEIZQY')
for idea in crypto_news:
    crypto_titles= idea.find_all('a', class_= 'Box-sc-1hpkeeg-0 hdfPqS')
    for bar in crypto_titles:
        if bar.text[:11] == 'Market Wrap':
            crypto_headlines.insert(0, bar.text.strip() + '.')
            crypto_links.insert(0, 'coindesk.com' + str(bar['href']))
        else:
            crypto_headlines.append(bar.text.strip() + '.')
            crypto_links.append('coindesk.com' + str(bar['href']))

r = requests.get("https://www.marketwatch.com/investing/future/sp%20500%20futures")
soup = BeautifulSoup(r.content, 'lxml')

futures = soup.find_all('div', class_ = 'intraday__data')
for future in futures:
    future_index = future.find('bg-quote', class_ = 'value')
    future_change = future.find('span', class_ = 'change--percent--q')


# CoinTelegraph
scraper = cloudscraper.create_scraper()
r = scraper.get('https://cointelegraph.com/')
soup = BeautifulSoup(r.content, 'lxml')

crypto_news = soup.find_all('li', class_= 'posts-listing__item')
for idea in crypto_news:
    news_check= idea.find('span', class_= 'post-card__badge')
    if news_check:
        if news_check.text.strip() == 'News' or news_check.text.strip() == 'Market News' or news_check.text.strip() == 'Breaking news':
            these_links = idea.find_all('a', class_ = 'post-card__title-link')
            these_titles = idea.find_all('span', class_ = 'post-card__title')
            for bar in these_titles:
                if bar.text != '':
                    crypto_headlines.append(bar.text.strip() + '.')
            for link in these_links:
                crypto_links.append('cointelegraph.com' + str(link['href']))

#The Block
r = scraper.get("https://www.theblockcrypto.com/")
soup = BeautifulSoup(r.content, 'lxml')

block_links = soup.find_all('a', class_ = 'theme color-outer-space')
for each in block_links:
    crypto_headlines.append(each.text.strip() + '.')
    crypto_links.append('www.theblockcrypto.com' + str(each['href']))

nine_am_time = time(9,0,0)



with open(f'news.txt', 'w', encoding='utf-8') as f:
    f.write('Morning News\n')
    f.write(f'{date.today().strftime("%B %d, %Y")}\n')
    f.write(f'Singapore Time: {nine_am_time.strftime("%H:%M")} am\n\n')
    f.write(f'BTC: ${btc_price} ({btc_percentage_change}%)\n')
    f.write(f'ETH: ${eth_price} ({eth_percentage_change}%)\n')
    f.write(f'S&P500 Futures: ${future_index.text} ({future_change.text})\n')
     
    f.write('\nTraditional Finance\n')
    for i in range(len(final_headlines)):
        f.write(u'   \u2022')
        f.write(f'   {final_headlines[i]}\n')
        f.write(f'{final_links[i]}\n')

    f.write('\nCrypto\n')
    for i in range(len(crypto_headlines)):
        f.write(u'   \u2022')
        f.write(f'   {crypto_headlines[i]}\n')
        f.write(f'{crypto_links[i]}\n')
    
    f.write('\nDeal Flow\n')
