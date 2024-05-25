from bs4 import BeautifulSoup as bs
import requests

website = "https://subslikescript.com/movie/Titanic-120338"

result = requests.get(website)
content = result.text
soup = bs(content, "lxml")
print(soup.prettify())