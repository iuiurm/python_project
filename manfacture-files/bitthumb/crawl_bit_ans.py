import requests
from bs4 import BeautifulSoup

url = 'https://www.bithumb.com/'
response  = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

coins = soup.select('.coin_list tr')
for c in coins :
    cname = c.select_one('td:nth-child(1) p a strong').text #첫번째 있는 것만 가져 오겠다.
    cprice = c.select_one('td:nth-child(2) strong').text
    print (cname,cprice)

with open('bithumb.csv', 'w', encoding='utf-8') as f :
    for c in coins:
        cname = c.select_one('td:nth-child(1) p a strong').text.strip()  # 첫번째 있는 것만 가져 오겠다. strip은 공백을 지운다 스페이스.
        cprice = c.select_one('td:nth-child(2) strong').text.replace(',', '')

        f.write(f'{cname},{cprice} \n')

