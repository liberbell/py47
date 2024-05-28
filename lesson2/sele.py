from selenium import webdriver
import chromedriver_binary

website = "https://www.adamchoi.co.uk/corners/detailed"
path = "./chromedriver"
driver = webdriver.Chrome()

driver.get(website)