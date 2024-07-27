import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
titles = soup.find_all(name="h3", class_="title")

movies = [movie_title.get_text() for movie_title in titles]
movies.reverse()
for movie in movies:
    print(movie)


