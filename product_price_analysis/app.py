from flask import Flask, redirect, url_for, render_template, url_for, g, request
from jinja2 import Template
from jinja2 import Environment, Undefined
from jinja2.exceptions import UndefinedError
import sqlite3
import os
from price_analysis import FDataBase


# конфигурация
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path,'export_excel_all_time.db')))
app.config['SECRET_KEY'] = 'dawdajk74hh35md8lef832kj'


DATABASE = '/export_excel_all_time.db'
DEBUG = True
SECRET_KEY = 'fdgfh78@#5?>gfhf89dx,v06k'
#USERNAME = 'admin'
#PASSWORD = '123'

position = ["Еда", "Хлеб (батон)", "Овощи", "Крупы,макароны", "Печенье(конфеты и другое сладкое)", "Молочка(молоко,кефир,творог)", "Мясо(кура,гов,свинина,индейка)", "Пюре,йогурт детям.", "Ветчина(колбаса,сосиски)", "Вкусности детям", "Работа_еда", "Школа_питание", "Фрукты", "Рыба"]

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


menu = [{"name": "Анализировать цену за год!", "url": "year"},
        {"name": "Анализировать цену за месяц!", "url": "month"}]


def get_db():
    '''Соединение с БД, если оно еще не установлено'''
    if getattr(g, 'link_db', None) is None:
        g.link_db = connect_db()
    return g.link_db

 
@app.route("/index")
def index():
    db = get_db()
    dbase = FDataBase(db)
    print(url_for('index'))
    return render_template('index.html', menu = menu)


@app.teardown_appcontext
def close_db(error):
    '''Закрываем соединение с БД, если оно было установлено'''
    if getattr(g, 'link_db', None) is not None:
        g.link_db.close()

@app.route("/year", methods=["POST", "GET"])
def year():
    global choosing_year
    global res
    db = get_db()
    dbase = FDataBase(db)
    print(request.method)

    if request.method == 'POST':
        if len(request.form['choosing_year']) == 4:
            res = dbase.amount_for_year(request.form.get('choosing_year'))
        #print(request.form['choosing_year'])
        print(request.form.get('choosing_year'))
        #selected_year = request.form['choosing_year']
    print(url_for('year'))
    #return render_template('year.html')
    return render_template('year.html', price=dbase.amount_for_year(request.form.get('choosing_year')), selected_year=request.form.get('choosing_year'))

@app.route("/month", methods=["POST", "GET"])
def month():
    global choosing_year
    global choosing_month
    db = get_db()
    dbase = FDataBase(db)
    posit = ''

    if request.method == 'POST':
#        if len(request.form['choosing_year']) == 4 and len(request.form['choosing_month']) == 2:
#            res = dbase.monthly_amount(request.form.get('choosing_year'), request.form.get('choosing_month'))
        #print(request.form['Введите год'])
        print(request.form.get('choosing_month'))
        #print(request.form['choosing_month'])
        print(request.form.get('choosing_year'))
        #selected_year = request.form['choosing_year']
    #posit = render_template('month.html', posit=dbase.monthly_amount2(request.form.get('posit')))
    print(url_for('month'))
    #return render_template('month.html')
    return render_template('month.html', price=dbase.monthly_amount2(request.form.get('choosing_year'), request.form.get('choosing_month'), position), position_dict=dbase.monthly_amount(request.form.get('choosing_year'), request.form.get('choosing_month'), position), choosing_month=request.form.get('choosing_month'), choosing_year=request.form.get('choosing_year'))

if __name__ == "__main__":
    app.run(debug=True)