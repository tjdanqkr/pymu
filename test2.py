import requests
from bs4 import BeautifulSoup
webpage = requests.get("https://www.daangn.com/hot_articles")
soup = BeautifulSoup(webpage.content, "html.parser")
print(soup.div.text)
print('child')
for child in soup.ul.children:
    print(child)
print('parent')
for parent in soup.ul.parents:
    print(parent)
print('div')

for d in soup.div.children:
    print(d)
