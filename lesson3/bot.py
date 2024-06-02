from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from anti_useragent import UserAgent
import pandas as pd
import time

url = "https://www.audible.com/search"

options = Options()
# options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-agent=" + UserAgent("windows").chrome)

browser = webdriver.Chrome(options=options)
browser.get(url)
browser.implicitly_wait(2)
# print(browser.page_source)
# browser.maximize_window()

pagination = browser.find_element(By.XPATH, '/ul[contains(@class,"pagingElements")]/li')
pages = pagination.find_element(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)

current_page = 1
book_title = []
book_author = []
book_runtime = []

while current_page <= last_page:
    time.sleep(2)
    container = WebDriverWait
    container = browser.find_element(By.CLASS_NAME, "adbl-impression-container")
    products = container.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')

    for product in products:
        title = product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text
        book_title.append(title)
        print(title)
        book_author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
        book_runtime.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

    current_page = current_page + 1
    try:
        next_page = browser.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

# browser.quit()

df_books = pd.DataFrame({
    "title": book_title,
    "author": book_author,
    "runtime": book_runtime
    })

df_books.to_csv("books_headless.csv", index=False)