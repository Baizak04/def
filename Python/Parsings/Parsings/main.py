# import requests
# from bs4 import BeautifulSoup


# with open("index.html",encoding = "utf-8") as file:

#     src = file.read()
# # print(src) 

# soup = BeautifulSoup(src, "lxml")

# # title = soup.text
# # print(title)
# page_h1 = soup.find_all("h1")
# print(page_h1)

# 1) библотека боюнча окуп келуу:
# BeautifulSoup, requests


# import requests
# from bs4 import BeautifulSoup

# url = 'https://premier.one/video/movies'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')

# print(soup)
# f = soup.find_all("div",class_="/ntitle/n")
# for film in f:
#     film = film.find("a")
#     print(film.text)


# scraper.py

# scraper.py
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')

for quote in quotes:
    print(quote.text)
