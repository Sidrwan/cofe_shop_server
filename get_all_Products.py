from webapp import create_app
from webapp.shoko_product_parser import get_product_list
from config import PRODUCTS_URL_1, PRODUCTS_URL_2

app = create_app()
with app.app_context():
    get_product_list(PRODUCTS_URL_1)