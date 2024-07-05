from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

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

def get_data_ec():
    url_ec = "https://scraping.official.ec/"
    web_data = requests.get(url_ec)
    result = bs(web_data.text, "html.parser")

    item_list = result.find('ul', {'id': 'itemList'})
    items = item_list.findAll('li')

    data_ec = []
    for item in items:
        datum_ec = {} 
        datum_ec["title"] = item.find('p', {'class': 'items-grid_itemTitleText_5c97110f'}).text
        price = item.find('p', {'class': 'items-grid_price_5c97110f'}).text
        datum_ec["price"] = price.replace("¥", "").replace(",", "")
        datum_ec["link"] = item.find("a")["href"]
        is_stock = items[2].find("p", {"class": "items-grid_soldOut_5c97110f"}) == None
        datum_ec["is_stock"] = "Stock" if is_stock == True else "Sold out"
        data_ec.append(datum_ec)

    df_ec = pd.DataFrame(data_ec)
    return df_ec

print(get_data_udemy())
print(get_data_ec())
