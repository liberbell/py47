from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

url = "https://www.audible.com/search"

options = Options()
# options.add_argument("--headless=new")
options.add_argument("--window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.implicitly_wait(5)
browser.get(url)
# browser.maximize_window()

container = browser.find_element(By.CLASS_NAME, "adbl-impression-container")
products = container.find_elements(By.XPATH, './/li[contains(@class, "productListItem")]')

book_title = []
book_author = []
book_runtime = []
for product in products:
    title = product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text
    book_title.append(title)
    print(title)
    book_author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
    book_runtime.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

browser.quit()

df_books = pd.DataFrame({
    "title": book_title,
    "author": book_author,
    "runtime": book_runtime
    })

df_books.to_csv("books.csv", index=False)