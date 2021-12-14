# from collections import UserList
from os import name
import requests
from bs4 import BeautifulSoup
import re

# url="https://f1000research.com/articles/10-388"    #original url
# url='https://f1000research.com/articles/10-386'      #2nd Url

# url='https://f1000research.com/articles/10-1'         #12 author url
url='https://f1000research.com/articles/10-127'         #aswin bro url
page = requests.get(url)

soup = BeautifulSoup(page.content,'lxml')            #Lxml parser

full_class = soup.find_all('span',attrs={'class' : "js-article-affiliation"})       #container for author details

Author_ini = []                                      #Author inistitute collected list


for i in full_class:                        #this for load all author univercity detaiils to list
    Author_ini.append(i.text)



#Total container

class_new = soup.find('div',{'class' : "authors _mdl-layout js-article-authors"})

# span_emty = class_new.find_all('span',{'class' :""})

span_emty = class_new.find_all('span',{'class' :["","article-page-hidden-authors"]}) #call two class same time

all_details = []                            #output list


for i in span_emty:
    f = i.find('span',{'class':'js-article-author'})
    if f != None:
        v = f.text
        #call dic function
        
        k = {}

        k['author_name'] = v

        orc = i.find('a',{'id':re.compile("^author-orcid-")})
        if orc != None:
            orc_id = (orc.get('href'))
        else:
            orc_id = None

        k["orc_id"] = orc_id
        
        g = i.find('sup').text      #use to find sup tag values

        if len(g)>1:
        
            list_1 = []

            for f in g.split(','): #1-4
                
                if len(f) == 1:
            
                    list_1.append(Author_ini[int(f)-1])

                else:
                    new_list = f #1-4  
                    
                    for j in range(int(new_list[0]),(int(new_list[2])+1)):
                    
                        list_1.append(Author_ini[int(j)-1]) 
                
            k['author_ins']=list_1

        else:
            k['author_ins']=Author_ini[int(g)-1]
    



        all_details.append(k)
     
    
print(all_details)


