import requests
from bs4 import BeautifulSoup as b

def parser(url): # парсер своей персоной
    r = requests.get(url, allow_redirects=True, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        'Upgrade-Insecure-Requests': '1'
    })
    r.encoding = 'UTF-8' # Это может даже не понадобится, но на всякий случай. Впрошлый раз была кодировка ISO-8859-1.
    soup = b(r.text, 'html.parser')
    only_grades = soup.find_all('div', class_='cell-data')
    return [c.text for c in only_grades] # Это я так новости сортировал, но вроде пока актуально

session  = requests.Session() # начал сессию
data = {'login': (None, 'nina_129'), # Понаделал даты себе теперь я юзер
        'password': (None, 'K01112006k'),
        'return_url': (None, '/')}
UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0" # сделал агента007


html = session.get('https://school.nso.ru/authorize', headers={'User-Agent': UserAgent, 'Upgrade-Insecure-Requests': '1'}) # Получил страницу свою
url = 'https://school.nso.ru/journal-student-grades-action/u.982' # записал ссылку в переменную
authorization = session.post('https://school.nso.ru/ajaxauthorize', files=data) # вроде как авторизацию произвёл. Не уверен.
# Вроде как пароли логины эти дал, незнаю взял ли он их

grade = session.get(url, headers={'User-Agent': UserAgent, 'Upgrade-Insecure-Requests': '1'}) # типо оценки там получил (по факту ничё не получил)

mygrades = parser(url)

print(mygrades)
