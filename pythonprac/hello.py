import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:as123123@cluster0.nnsglfi.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
movies = soup.select('#old_content > table > tbody > tr')
for movie in movies:
    a = movie.select_one('td.title > div > a')
    b = movie.select_one('td.point')
    if a is not None:
        title = a.text
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        star = b.text
        doc = {
            'title':title,
            'rank':rank,
            'star':star
        }
        db.movies.insert_one(doc)
# 코딩 시작
#old_content > table > tbody > tr:nth-child(3) > td.point
#old_content > table > tbody > tr:nth-child(3) > td:nth-child(1) > img