from flask import Flask, render_template

from cofe_parser import get_cofe_list


app = Flask(__name__)

@app.route("/")
def index():
    title = 'Меню кофе'
    cofe_list = get_cofe_list()
    return render_template('index.html', page_title=title, cofe_list=cofe_list)

if __name__=="__main__":
    app.run(debug=True)