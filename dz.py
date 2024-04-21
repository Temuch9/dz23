import requests
from bs4 import BeautifulSoup

url='https://stopgame.ru/'
response = requests.get(url)
print(response.status_code)
print(response.text)
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)

print(soup.a)
print(soup.a.string)

img_tags = soup.find_all('img')
for img_tags in img_tags:
    print(img_tags)

a_tags = soup.find_all('a')
for a_tags in a_tags:
    print(a_tags)

title_tags = soup.find_all('title')
for title_tags in title_tags:
    print(title_tags)

big_body_div = soup.find( 'div', class_ = 'modulebody1')
print(big_body_div)