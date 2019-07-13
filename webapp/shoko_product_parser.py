from datetime import datetime
from .products_list import PRODUCTS_LINK_LIST
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
        all_product_list = soup.findAll('div', class_='product-card__inner')
        result_product_list = []
        for item in all_product_list:
            image_link = 'https://shoko.ru' + item.find('img')['data-src']
            title = item.find('h4').text
            price = item.find('span').text
            

            save_Products(title=title, price=price, image_link=image_link)



def save_Products(title, price, image_link,):
    Products_exists = Products.query.filter(Products.image == image_link).count()
    if not Products_exists:
        new_Products = Products(title=title, price=price, image=image_link,)
        db.session.add(new_Products)
        db.session.commit()


def get_all_products(link_list):
    for link in link_list:
        get_product_list(link)