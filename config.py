import os

basedir = os.path.abspath(os.path.dirname(__file__))

PRODUCTS_URL_1 = 'https://shoko.ru/menu/kofe/'
PRODUCTS_URL_2 = 'https://shoko.ru/menu/sendvichi-i-omlety/'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')