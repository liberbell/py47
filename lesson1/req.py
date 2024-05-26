from bs4 import BeautifulSoup as bs
import requests
import time

root = "https://subslikescript.com"
website = "https://subslikescript.com/movie/Titanic-120338"
website2 = f"{root}/movies"

result = requests.get(website2)
content = result.text
soup = bs(content, "lxml")
# print(soup.prettify())

box = soup.find("article", class_="main-article")
links = []
for link in box.find_all("a", href=True):
    time.sleep(0.5)
    links.append(link["href"])

# print(links)

for link in links:
    website = f"{root}/{link}"
    # print(website)
    result = requests.get(website)
    content = result.text
    print(content)

#     box = soup.find("article", class_="main-article")

#     title = box.find("h1").get_text()
#     transcript = box.find("div", class_="full-script").get_text(strip=True, separator=" ")

#     with open(f"{title}.txt", "w") as file:
#         file.write(transcript)