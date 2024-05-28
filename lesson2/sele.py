from selenium import webdriver

website = "https://www.adamchoi.co.uk/corners/detailed"
path = "./chromedriver"
driver = webdriver.Chrome(path)

driver.get(website)