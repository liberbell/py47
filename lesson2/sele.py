from selenium import webdriver
import chromedriver_binary
# pip install chromedriver-binary==125.0.6422.78.0

website = "https://www.adamchoi.co.uk/corners/detailed"
# path = "./chromedriver"
driver = webdriver.Chrome()

driver.get(website)
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')

driver.quit()

# //*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]