from bs4 import BeautifulSoup as bs
import requests

url = "https://scraping-for-beginner.herokuapp.com/udemy"
web_data = requests.get(url)

# print(web_data.text)
result = bs(web_data.text, "html.parser")
# print(result)

n_subscriber = result.find('p', {'class': 'subscribers'}).text
print(n_subscriber.split("：")[1])

n_subscriber = int(n_subscriber.split("：")[1])

n_review = result.find('p', {'class': 'reviews'}).text
print(n_review.split("：")[1])