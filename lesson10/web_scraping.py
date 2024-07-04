from bs4 import BeautifulSoup as bs
import requests

url = "https://scraping-for-beginner.herokuapp.com/udemy"
web_data = requests.get(url)

# print(web_data.text)
result = bs(web_data.text, "html.parser")
# print(result)

n_subscriber = result.find('p', {'class': 'subscribers'}).text
n_subscriber = int(n_subscriber.split("：")[1])
# print(n_subscriber)

n_review = result.find('p', {'class': 'reviews'}).text
n_review =int(n_review.split("：")[1])
# print(n_review)

url_ec = "https://scraping.official.ec/"
web_data = requests.get(url_ec)
result = bs(web_data.text, "html.parser")

item_list = result.find('ul', {'id': 'itemList'})
# print(item_list)
items = item_list.findAll('li')
item = items[0]
title = item.find('p', {'class': 'items-grid_itemTitleText_5c97110f'}).text