import requests
from bs4 import BeautifulSoup
url="https://f1000research.com/articles/4-1522"
result=requests.get(url)
#print(result.content)
#align = requests(result.content)
#print(align.prettify())
soup = BeautifulSoup(result.content,'lxml')
#print(soup.prettify())
#print(soup)   
Title=soup.find('meta',attrs = {'name':'dc.title'})['content']
#Artical_type =soup.find("div",attrs={'class':"artical-type artical-display"}).text
pdf_url=soup.find('meta',attrs = {'name':'prism.url'})['content']
citation_author=soup.find('meta',attrs = {'name':'citation_author'})['content']
citation_volume=soup.find('meta',attrs = {'name':'citation_volume'})['content']
citation_publication_number=soup.find('meta',attrs = {'name':'citation_publication_number'})['content']
citation_keywords=soup.find('meta',attrs = {'name':'citation_keywords'})['content']
prism_publicationDate=soup.find('meta',attrs = {'name':'prism.publicationDate'})['content']
description=soup.find('meta',attrs = {'name':'dc.description'})['content']
citation_description=soup.find('meta',attrs = {'name':'citation_description'})['content']
citation_abstract=soup.find('meta',attrs = {'name':'citation_abstract'})['content']
#print(pdf_url)
#print(Title)



scraping_dict={}
scraping_dict['Title']=Title
scraping_dict['pdf_url']=pdf_url
scraping_dict['citation_author']=citation_author
scraping_dict['citation_volume']=citation_volume
scraping_dict['prism_publicationDate']=prism_publicationDate
scraping_dict['description']=description
scraping_dict['citation_abstract']=citation_abstract
scraping_dict['citation_description']=citation_description
print(scraping_dict)
print(pdf_url)
print(citation_author)
print(citation_volume)

print(citation_keywords)
print(prism_publicationDate)
print(description)
print(citation_description)
print(citation_publication_number)
print(citation_abstract)