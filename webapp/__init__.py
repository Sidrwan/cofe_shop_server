from flask import Flask, render_template
from webapp.forms import LoginForm
from webapp.models import db, Products

from webapp.shoko_product_parser import get_product_list


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def index():
        title = 'Меню Fake Шоколадницы '
        Products_list = Products.query.all()
        return render_template('index.html', page_title=title, Products_list=Products_list)

    @app.route('/login')
    def login():
        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    return app