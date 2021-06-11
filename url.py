import requests
from bs4 import BeautifulSoup
 
 
url = 'https://f1000research.com/browse/articles'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
url_s=soup.find_all('a',class ="artical-link")
 
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))