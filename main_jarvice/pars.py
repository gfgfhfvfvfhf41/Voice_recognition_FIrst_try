import requests
from bs4 import BeautifulSoup as BS
import webbrowser as w

while True:
    jk = input("v: ")

    r = requests.get("https://e1.zona.plus/search/" + jk)
    html = BS(r.text, 'lxml')

    b = {}

    bg = html.findAll("a", class_="results-item", itemprop="url")
    for n in bg:
        gh = n.get('title').lower()
        if  jk in gh:
            b[gh] = "https://e1.zona.plus" + n.get("href")

    for key,value in b.items():
        print(key + "\n" + value + "\n")
        w.open(value)

