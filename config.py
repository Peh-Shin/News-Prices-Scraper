import os
from selenium import webdriver

os.environ["PATH"] += (
    os.pathsep + r"C:\\Users\\peh_s\\OneDrive\\Documents\\Selenium Drivers"
)  
url = "https://www.coindesk.com/"
delay = 30

driver = webdriver.Chrome()

driver.implicitly_wait(delay)
driver.get(url)
coindesk_html = driver.page_source
driver.quit()