from webapp import create_app
from webapp.products_list import PRODUCTS_LINK_LIST
from webapp.shoko_product_parser import get_all_products

app = create_app()
with app.app_context():
    get_all_products(PRODUCTS_LINK_LIST)