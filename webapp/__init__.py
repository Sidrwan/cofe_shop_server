from flask import Flask, render_template

from webapp.model import db, Products

from webapp.shoko_product_parser import get_product_list


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def index():
        title = 'Меню Fake Шоколадницы '
        kofe_list = get_product_list(app.config['PRODUCTS_URL_1'])
        shavarma_list = get_product_list(app.config['PRODUCTS_URL_2'])
        return render_template('index.html', page_title=title, kofe_list=kofe_list, shavarma_list=shavarma_list)

    return app