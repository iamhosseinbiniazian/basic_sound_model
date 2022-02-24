from bs4 import BeautifulSoup
import requests
page = requests.get("https://docs.continuum.io/anaconda/packages/pkg-docs")
soup = BeautifulSoup(page.content, 'html.parser')
table=soup.find(lambda tag:tag.name=='table')
atag=table.findAll(lambda tag: tag.name=='a')
for tags in atag:
    print(tags.contents)