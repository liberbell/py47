from bs4 import BeautifulSoup as bs
import requests

# data_udemy = {}/

def get_data_udemy():
    url = "https://scraping-for-beginner.herokuapp.com/udemy"
    web_data = requests.get(url)
    result = bs(web_data.text, "html.parser")

    n_subscriber = result.find('p', {'class': 'subscribers'}).text
    n_subscriber = int(n_subscriber.split("：")[1])
    n_review = result.find('p', {'class': 'reviews'}).text
    n_review =int(n_review.split("：")[1])
    return {
        "n_subscriber": n_subscriber,
        "n_review": n_review
    }

print(get_data_udemy())