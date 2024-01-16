import requests
from bs4 import BeautifulSoup as b
#https://shkola2-spektr.edusite.ru/?ysclid=lrgc0stor2997015105
url = 'https://shkola2-spektr.edusite.ru/?ysclid=lrgc0stor2997015105'
def parser(url):
    r = requests.get(url, allow_redirects=True, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    })
    r.encoding = 'UTF-8'
    soup = b(r.text, 'html.parser')
    only_news = soup.find_all('div', class_='news-text')
    return [c.text for c in only_news]
news = parser(url)
news_text = []
# for i in range(len(news)-1):
#     news_text[i] = news[i].replace('\xa0', '')
print(news)