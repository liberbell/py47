from selenium import webdriver
import chromedriver_binary
# pip install chromedriver-binary==125.0.6422.78.0
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = "https://www.adamchoi.co.uk/overs/detailed"
# path = "./chromedriver"
browser = webdriver.Chrome()
browser.get(website)

all_matches_button = browser.find_element(By.XPATH, "//label[@analytics-event='All matches']")
all_matches_button.click()

dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("Spain")

time.sleep(2)

matches = browser.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    # print(match.text)
    date.append(match.find_element(By.XPATH, "./td[1]").text)
    # home = home_team.append(match.find_element(By.XPATH, "./td[2]").text)
    home = match.find_element(By.XPATH, "./td[2]").text
    home_team.append(home)
    print(home)
    score.append(match.find_element(By.XPATH, "./td[3]").text)
    away_team.append(match.find_element(By.XPATH, "./td[4]").text)
browser.quit()

# //*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]
# //*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]
# /html/body/div[2]/div/div/div[2]/div/home-away-selector/div/div/div/div/label[2]
# <label class="btn btn-sm btn-primary ng-untouched ng-valid ng-not-empty ng-dirty active ng-valid-parse" data-ng-model="hasc.$scope.doShowSplit" data-btn-radio="false" analytics-on="click" analytics-event="All matches" analytics-category="Detailed pages filters" analytics-label="Home Away Selector">All matches</label>

df = pd.DataFrame({
    'date': date,
    'home_team': home_team,
    'score': score,
    'away_team': away_team
    })
df.to_csv("football_data.csv", index=False)
print(df)