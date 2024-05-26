from bs4 import BeautifulSoup as bs
import requests

website = "https://subslikescript.com/movie/Titanic-120338"
website2 = "https://subslikescript.com/movies"

result = requests.get(website)
content = result.text
soup = bs(content, "lxml")
# print(soup.prettify())

box2 = soup.find("article", class_="main-article")
box.find_all("a", href=True)
# box = soup.find("article", class_="main-article")
# title = box.find("h1").get_text()
# transcript = box.find("div", class_="full-script").get_text(strip=True, separator=" ")

with open("titanic.txt", "w") as file:
    file.write(transcript)