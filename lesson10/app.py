from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from google.oauth2.service_account import Credentials
import gspread
import datetime
from gspread_dataframe import set_with_dataframe
import altair as alt

# data_udemy = {}/
today = datetime.date.today().strftime("%Y/%m/%d")

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

def get_worksheet():
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

    return worksheet

worksheet = get_worksheet()
data = worksheet.get_all_values()
df_udemy = pd.DataFrame(data[1:], columns=data[0])

df_udemy = df_udemy.astype({
    "n_subscriber": int,
    "n_review": int
})
ymin1 = df_udemy["n_subscriber"].min()-10
ymax1 = df_udemy["n_subscriber"].min()+10
ymin2 = df_udemy["n_review"].min()-10
ymax2 = df_udemy["n_review"].min()+10

base = alt.Chart(df_udemy).encode(
    alt.X('date:T', axis=alt.Axis(title=None))
)

line1 = base.mark_line(opacity=0.3, color='#57A44C').encode(
    alt.Y('n_subscriber',
          axis=alt.Axis(title="Subscriber number", titleColor='#57A44C'),
          scale=alt.Scale(domain=[ymin1, ymax1])
          )
)

line2 = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
    alt.Y("n_review",
          axis=alt.Axis(title="Reviewers", titleColor='#5276A7'),
          scale=alt.Scale(domain=[ymin2, ymax2])
          )
)


data_udemy = get_data_udemy()

data_udemy["date"] = today

df = pd.concat([df, pd.DataFrame([data_udemy])], ignore_index=True)

first_row = 1
set_with_dataframe(worksheet, df, row=1, col=1)

def main():
    

if __name__ == "__main__":
    main()

# data = worksheet.get_all_values()
# df_udemy = pd.DataFrame(data[1:], columns=data[0])

# df_udemy = df_udemy.astype({
#     "n_subscriber": int,
#     "n_review": int
# })

# ymin1 = df_udemy["n_subscriber"].min()-10
# ymax1 = df_udemy["n_subscriber"].min()+10

# ymin2 = df_udemy["n_review"].min()-10
# ymax2 = df_udemy["n_review"].min()+10

# print(type(ymin2), type(ymax2))

# base = alt.Chart(df_udemy).encode(
#     alt.X('date:T', axis=alt.Axis(title=None))
# )

# line1 = base.mark_line(opacity=0.3, color='#57A44C').encode(
#     alt.Y('n_subscriber',
#           axis=alt.Axis(title="Subscriber number", titleColor='#57A44C'),
#           scale=alt.Scale(domain=[ymin1, ymax1])
#           )
# )

# line2 = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
#     alt.Y("n_review",
#           axis=alt.Axis(title="Reviewers", titleColor='#5276A7'),
#           scale=alt.Scale(domain=[ymin2, ymax2])
#           )
# )

# chart = alt.layer(line1, line2).resolve_scale(
#     y='independent'
# )

