import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:as123123@cluster0.nnsglfi.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

genies = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for genie in genies:
    title = genie.select_one('td.info > a.title.ellipsis').text.strip()
    rank = genie.select_one('td.number').text[0:2].strip()
    artist = genie.select_one('td.info > a.artist.ellipsis').text
    print(rank, title,artist)

