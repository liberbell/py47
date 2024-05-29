from selenium import webdriver
import chromedriver_binary
# pip install chromedriver-binary==125.0.6422.78.0
from selenium.webdriver.common.by import By

website = "https://www.adamchoi.co.uk/overs/detailed"
# path = "./chromedriver"
driver = webdriver.Chrome()

driver.get(website)
all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements(By.TAG_NAME, 'tr')
driver.quit()

# //*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]