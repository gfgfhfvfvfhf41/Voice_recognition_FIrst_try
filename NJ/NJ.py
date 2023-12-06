import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://w127.zona.plus/search/%D0%BE%D0%B4%D0%B8%D0%BD%20%D0%B4%D0%BE%D0%BC%D0%B0")
html = BS(r.content, 'html-parser')

for a in html.select(".results > .results-item-wrap"):
    title = a.select('/caption > a')
    print(title[0].text)