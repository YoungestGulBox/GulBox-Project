import requests
from bs4 import BeautifulSoup

req = requests.get('https://finance.naver.com/item/fchart.naver?code=035720')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_stock = soup.select(
    'aside_section cop_list'
)

for stock_name in my_stock:
    print(stock_name.text)