import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls055386972/'

# 1. Get the HTML page with HTTP request
response = requests.get(url, headers={"Accept-Language": "en-US"})
data = response.content
# print(data)

# 2. use Beautiful soup to decifer/search the HTML
soup = BeautifulSoup(data, 'html.parser')

movies = soup.find_all('div', class_='lister-item-content')
# print(movie)
for movie in movies:
    title = movie.find('h3').find('a').string
    duration = int(movie.find('span', class_='runtime').string.strip(" min"))
    print(title, duration)