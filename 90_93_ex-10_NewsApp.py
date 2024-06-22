import requests
import json


query = input("What type of news are you interested in: ")


url = f"https://newsapi.org/v2/everything?q={query}&from=2024-03-01&sortBy=publishedAt&apiKey=5dee70f006eb464bb7276d55ee4d7b7d"

response = requests.get(url)
news = json.loads(response.text)
# print(news)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------------------------------------------------------")

