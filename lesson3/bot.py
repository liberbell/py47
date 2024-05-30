from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By

url = "https://www.audible.com/search"

browser = webdriver.Chrome()
browser.get(url)
browser.maxmize_window()

container = browser.find_element(By.CLASS_NAME, "adbl-impression-container")
products = container.find_element(By.XPATH, "./li")

for product in products:
    product.find_element(By.XPATH, '//h3[contains(@class, "bc-heading")]').text