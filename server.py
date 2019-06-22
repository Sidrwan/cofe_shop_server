from flask import Flask, render_template

from shoko_product_parser import get_product_list


app = Flask(__name__)

@app.route("/")
def index():
    title = 'Меню Fake Шоколадницы '
    kofe_list = get_product_list("https://shoko.ru/menu/kofe/")
    shavarma_list = get_product_list("https://shoko.ru/menu/sendvichi-i-omlety/")
    return render_template('index.html', page_title=title, kofe_list=kofe_list, shavarma_list=shavarma_list)

if __name__=="__main__":
    app.run(debug=True)