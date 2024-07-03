from bs4 import BeautifulSoup as bs
import requests

url = "https://scraping-for-beginner.herokuapp.com/udemy"
web_data = requests.get(url)

# print(web_data.text)
result = bs(web_data.text, "html.parser")
# print(result)

print(result.find('p', {'class': 'subscribers'}).text)