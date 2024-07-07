from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from google.oauth2.service_account import Credentials
import gspread
import datetime
from gspread_dataframe import set_with_dataframe
import altair as alt

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


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
credentials = Credentials.from_service_account_file(
    'service_account.json',
    scopes=scopes
)
gc = gspread.authorize(credentials)

SP_SHEET_KEY = '1C-278Mp-exInLJ1jpkaienNeAjXUNRGmEI_-T5jSH10'

sh = gc.open_by_key(SP_SHEET_KEY)
SP_SHEET = "db"
worksheet = sh.worksheet(SP_SHEET)
data = worksheet.get_all_values()
df = pd.DataFrame(data[1:], columns=data[0])

data_udemy = get_data_udemy()

# print(get_data_udemy())
# print(get_data_ec())

today = datetime.date.today().strftime("%Y/%m/%d")
data_udemy["date"] = today
print(data_udemy)

# df.append(data_udemy, ignore_index=True)
df = pd.concat([df, pd.DataFrame([data_udemy])], ignore_index=True)
print(df)

first_row = 1
set_with_dataframe(worksheet, df, row=1, col=1)

data = worksheet.get_all_values()
df_udemy = pd.DataFrame(data[1:], columns=data[0])

base = alt.Chart(df_udemy).encode(
    alt.X('date:T', axis=alt.Axis(title=None))
)

line1 = base.mark_line(opacity=0.3, color='#57A44C').encode(
    alt.Y('average(temp_max)').title('Avg. Temperature (°C)', titleColor='#57A44C'),
    alt.Y2('average(temp_min)')
)

line2 = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
    alt.Y('average(precipitation)').title('Precipitation (inches)', titleColor='#5276A7')
)

alt.layer(line1, line2).resolve_scale(
    y='independent'
)