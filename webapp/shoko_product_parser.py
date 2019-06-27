import requests
from bs4 import BeautifulSoup

from webapp.models import db, News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def get_product_list(url):
    html = get_html(url)
    if html:
        soup = BeautifulSoup(html, 'html5lib')
        all_product_list = soup.findAll('div', class_='product-card__inner')
        result_product_list = []
        for item in all_product_list:
            image_link = 'https://shoko.ru' + item.find('img')['data-src']
            title = item.find('h4').text
            price = item.find('div', class_='price').text.split()[0]

            result_product_list.append({
                'title': title,
                'picture': image_link,
                'price': price,
            })

            
        return result_product_list

