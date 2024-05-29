from selenium import webdriver
import chromedriver_binary
# pip install chromedriver-binary==125.0.6422.78.0
from selenium.webdriver.common.by import By

website = "https://www.adamchoi.co.uk/overs/detailed"
# path = "./chromedriver"
driver = webdriver.Chrome()

driver.get(website)
# all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements(By.TAG_NAME, 'tr')
print(matches)
for match in matches:
    print(match.text)
driver.quit()

# //*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]
# //*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]
# /html/body/div[2]/div/div/div[2]/div/home-away-selector/div/div/div/div/label[2]
# <label class="btn btn-sm btn-primary ng-untouched ng-valid ng-not-empty ng-dirty active ng-valid-parse" data-ng-model="hasc.$scope.doShowSplit" data-btn-radio="false" analytics-on="click" analytics-event="All matches" analytics-category="Detailed pages filters" analytics-label="Home Away Selector">All matches</label>