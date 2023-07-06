import requests
from bs4 import BeautifulSoup

url = 'https://www.op.gg/leaderboards/tier'
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")
txtall = soup.find_all('strong', class_="summoner-name")
text_list = []
for a in txtall:
    txt = a.text
    if txt:
        text_list.append(txt)

print(text_list)
