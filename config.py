import os
from selenium import webdriver

os.environ["PATH"] += (
    os.pathsep + r"C:\\Users\\peh_s\\OneDrive\\Documents\\Selenium Drivers"
)
url = "https://www.coindesk.com/"

driver = webdriver.Chrome()

driver.get(url)
driver.implicitly_wait(30)
coindesk_html = driver.page_source
driver.quit()