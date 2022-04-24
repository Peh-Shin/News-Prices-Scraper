import os
from selenium import webdriver

os.environ["PATH"] += (
    os.pathsep + r"C:\\Users\\peh_s\\OneDrive\\Documents\\Selenium Drivers"
)
url = "https://www.coindesk.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
coindesk_html = driver.page_source
driver.quit()
