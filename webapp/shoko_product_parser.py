from datetime import datetime

import requests
from bs4 import BeautifulSoup

from webapp.models import db, Products

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
        all_product_list = soup.findAll('div', class_=['product-card__inner','sideInnerText'])
        result_product_list = []
        for item in all_product_list:
            image_link = 'https://shoko.ru' + item.find('img')['data-src']
            title = item.find('h4').text
            price = item.find('span').text
            description = item.find('p').text
            print(description)
            

            save_Products(title=title, price=price, image_link=image_link, description=description)



def save_Products(title, price, image_link, description):
    Products_exists = Products.query.filter(Products.image == image_link).count()
    if not Products_exists:
        new_Products = Products(title=title, price=price, image=image_link, description=description)
        db.session.add(new_Products)
        db.session.commit()