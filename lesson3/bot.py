from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://www.audible.com/search"

browser = webdriver.Chrome()
browser.get(url)
browser.maxmize_window()

container = browser.find_element(By.CLASS_NAME, "adbl-impression-container")
products = container.find_element(By.XPATH, "./li")

book_title = []
book_author = []
book_runtime = []
for product in products:
    book_title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
    book_runtime.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

brower.quit()