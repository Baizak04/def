import requests

link = "https:\\icanbazip.com"
responce = requests.get(link).text
print(responce)