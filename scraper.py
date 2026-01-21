import requests
from bs4 import BeautifulSoup
import json
from pymongo import MongoClient
from utils import clean_text, parse_date

config = {}

with open('config.json', encoding='utf-8') as f:
    config = json.load(f)

RSS_URLS = config["rss_urls"]
KEYWORDS = config["keywords"]

client = MongoClient("mongodb://localhost:27017/")
db = client["news_db"]
collection = db["articles"]

all_articles = []

for url in RSS_URLS:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')

    for item in items:
        title = clean_text(item.title.text)
        link = item.link.text
        pub_date = parse_date(item.pubDate.text)
        description = clean_text(item.description.text) if item.description else ""

        if any(keyword.lower() in title.lower() for keyword in KEYWORDS):
            article = {
                "title": title,
                "link": link,
                "pub_date": pub_date,
                "description": description
            }
            all_articles.append(article)
            collection.update_one({"link": link}, {"$set": article}, upsert=True)

with open('articles.json', 'w', encoding='utf-8') as f:
    json.dump(all_articles, f, ensure_ascii=False, indent=4)

print(f"{len(all_articles)} articles sauvegardés !")
