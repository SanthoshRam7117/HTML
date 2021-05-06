import requests
url1 = requests.get("https://f1000research.com/articles/4-1522")
print(url1.abstract)