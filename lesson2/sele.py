from selenium import webdriver
import chromedriver_binary
# pip install chromedriver-binary==125.0.6422.78.0

website = "https://www.adamchoi.co.uk/corners/detailed"
# path = "./chromedriver"
driver = webdriver.Chrome()

driver.get(website)

driver.quit()