from flask import Blueprint, render_template, request, session, redirect, current_app, jsonify
from functools import wraps
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path

rgz = Blueprint('rgz',__name__)

products = [
    {
        'id': 1,
        'name': 'Кресло "Комфорт"',
        'description': 'Удобное кресло для отдыха',
        'price': 15000,
        'img_url': '/static/rgz/кресло_комфорт.jpg'
    },
    {
        'id': 2,
        'name': 'Диван "Люкс"',
        'description': 'Комфортный диван для гостиной',
        'price': 50000,
        'img_url': '/static/rgz/диван_люкс.jpg'
    },
    {
        'id': 3,
        'name': 'Стол "Деревянный"',
        'description': 'Прочный обеденный стол',
        'price': 20000,
        'img_url': '/static/rgz/стол_деревянный.jpg'
    },
    {
        'id': 4,
        'name': 'Стул "Минимализм"',
        'description': 'Стильный стул для кухни',
        'price': 5000,
        'img_url': '/static/rgz/стул_минимализм.jpg'
    },
    {
        'id': 5,
        'name': 'Кровать "Альви"',
        'description': 'Комфортная кровать для спальни',
        'price': 35000,
        'img_url': '/static/rgz/кровать_альви.jpg'
    },
    {
        'id': 6,
        'name': 'Шкаф "Вместительный"',
        'description': 'Просторный шкаф для одежды',
        'price': 40000,
        'img_url': '/static/rgz/шкаф_вместительный.jpg'
    },
    {
        'id': 7,
        'name': 'Тумба "Компактная"',
        'description': 'Маленькая тумба для хранения',
        'price': 8000,
        'img_url': '/static/rgz/тумба_компактная.jpg'
    },
    {
        'id': 8,
        'name': 'Стеллаж "Книжный"',
        'description': 'Стеллаж для книг и декора',
        'price': 12000,
        'img_url': '/static/rgz/стеллаж_книжный.jpg'
    },
    {
        'id': 9,
        'name': 'Кухонный гарнитур',
        'description': 'Полный комплект для кухни',
        'price': 120000,
        'img_url': '/static/rgz/кухонный гарнитур.jpg'
    },
    {
        'id': 10,
        'name': 'Комод "Классический"',
        'description': 'Комод с четырьмя ящиками',
        'price': 18000,
        'img_url': '/static/rgz/комод_классический.jpg'
    },
    {
        'id': 11,
        'name': 'Кресло-качалка',
        'description': 'Удобная качалка для отдыха',
        'price': 25000,
        'img_url': '/static/rgz/кресло-качалка.jpg'
    },
    {
        'id': 12,
        'name': 'Обеденный стол "Круглый"',
        'description': 'Круглый стол для небольшой семьи',
        'price': 15000,
        'img_url': '/static/rgz/обеденный стол_круглый.jpg'
    },
    {
        'id': 13,
        'name': 'Стул "Металлический"',
        'description': 'Стул с металлическим каркасом',
        'price': 6000,
        'img_url': '/static/rgz/стул_металлический.jpg'
    },
    {
        'id': 14,
        'name': 'Кровать "Односпальная"',
        'description': 'Компактная кровать для гостевой комнаты',
        'price': 20000,
        'img_url': '/static/rgz/кровать_односпальная.jpg'
    },
    {
        'id': 15,
        'name': 'Шкаф "Угловой"',
        'description': 'Угловой шкаф для небольших помещений',
        'price': 30000,
        'img_url': '/static/rgz/шкаф_угловой.jpg'
    },
    {
        'id': 16,
        'name': 'Тумба "Под телевизор"',
        'description': 'Тумба для размещения телевизора',
        'price': 10000,
        'img_url': '/static/rgz/тумба_под телевизор.jpg'
    },
    {
        'id': 17,
        'name': 'Стеллаж "Многоярусный"',
        'description': 'Стеллаж с несколькими уровнями',
        'price': 15000,
        'img_url': '/static/rgz/стеллаж_многоярусный.jpg'
    },
    {
        'id': 18,
        'name': 'Кухонный уголок','description': 'Комплект для небольшой кухни',
        'price': 80000,
        'img_url': '/static/rgz/кухонный уголок.jpg'
    },
    {
        'id': 19,
        'name': 'Комод "Современный"',
        'description': 'Комод с глянцевым покрытием',
        'price': 22000,
        'img_url': '/static/rgz/комод_современный.jpg'
    },
    {
        'id': 20,
        'name': 'Кресло "Бархатное"',
        'description': 'Кресло с бархатной обивкой',
        'price': 18000,
        'img_url': '/static/rgz/кресло_бархатное.jpg'
    },
    {
        'id': 21,
        'name': 'Обеденный стол "Прямоугольный"',
        'description': 'Прямоугольный стол для большой семьи',
        'price': 25000,
        'img_url': '/static/rgz/обеденный стол_прямоугольный.jpg'
    },
    {
        'id': 22,
        'name': 'Стул "Деревянный"',
        'description': 'Стул из натурального дерева',
        'price': 7000,
        'img_url': '/static/rgz/стул_деревянный.jpg'
    },
    {
        'id': 23,
        'name': 'Кровать "Детская"',
        'description': 'Кровать для детской комнаты',
        'price': 25000,
        'img_url': '/static/rgz/кровать_детская.jpg'
    },
    {
        'id': 24,
        'name': 'Шкаф "Платяной"',
        'description': 'Шкаф с полками и вешалками',
        'price': 45000,
        'img_url': '/static/rgz/шкаф_платяной.jpg'
    },
    {
        'id': 25,
        'name': 'Тумба "Подставка"',
        'description': 'Тумба для декоративных предметов',
        'price': 9000,
        'img_url': '/static/rgz/тумба_подставка.jpg'
    },
    {
        'id': 26,
        'name': 'Стеллаж "Узкий"',
        'description': 'Узкий стеллаж для узких пространств',
        'price': 13000,
        'img_url': '/static/rgz/стеллаж_узкий.jpg'
    },
    {
        'id': 27,
        'name': 'Кухонный стол',
        'description': 'Стол для небольшой кухни',
        'price': 12000,
        'img_url': '/static/rgz/кухонный стол.jpg'
    },
    {
        'id': 28,
        'name': 'Комод "Мини"',
        'description': 'Компактный комод для маленьких комнат',
        'price': 15000,
        'img_url': '/static/rgz/комод_мини.jpg'
    },
    {
        'id': 29,
        'name': 'Стул "Металлик"',
        'description': 'Стул с металлическим покрытием',
        'price': 7500,
        'img_url': '/static/rgz/стул_металлик.jpg'
    },
    {
        'id': 30,
        'name': 'Кровать "Стандарт"',
        'description': 'Компактная кровать для спальни',
        'price': 22000,
        'img_url': '/static/rgz/кровать_стандарт.jpg'
    },
    {
        'id': 31,
        'name': 'Шкаф "Мини"',
        'description': 'Небольшой шкаф для хранения вещей',
        'price': 18000,
        'img_url': '/static/rgz/шкаф_мини.jpg'
    },
    {
        'id': 32,
        'name': 'Тумба "Подсветка"',
        'description': 'Тумба с подсветкой для гостиной',
        'price': 12000,
        'img_url': '/static/rgz/тумба_подсветка.jpg'
    }
]

@rgz.route('/rgz/')
def lab_5():
    return render_template('rgz/rgz.html', login=session.get('login'), user_name=session.get('user_name'), products=products)

def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host='127.0.0.1',      
            database='oparina_rgz',  
            user='oparina_rgz',        
            password='4321' 
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@rgz.route('/rgz/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('rgz/register.html')

    login = request.form.get('login')
    password = request.form.get('password')
    user_name = request.form.get('name')
    phone = request.form.get('phone')
    if not (login and password and user_name and phone):
        return render_template('rgz/register.html', error="Пожалуйста, заполните все поля")

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT login FROM users WHERE login=%s;", (login,))
    else:
        cur.execute("SELECT login FROM users WHERE login=?;", (login,))

    if cur.fetchone():
        db_close(conn, cur)
        return render_template('rgz/register.html', error="Такой пользователь уже существует")

    password_hash = generate_password_hash(password)

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("INSERT INTO users (login, password, user_name, phone) VALUES (%s, %s, %s, %s);",
                    (login, password_hash, user_name, phone))
    else:
        cur.execute("INSERT INTO users (login, password, user_name, phone) VALUES (?, ?, ?, ?);",
                    (login, password_hash, user_name, phone))

    db_close(conn, cur)

    session['login'] = login
    session['user_name'] = user_name

    return render_template('rgz/rgzok.html', login=login)

@rgz.route('/rgz/logout')
def logout():
    session.pop('login', None)
    return redirect('/rgz/')

@rgz.route('/rgz/login', methods=['GET', 'POST'])
def login_5():
    if request.method == 'GET':
        return render_template('rgz/login.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not (login and password):
        return render_template('rgz/login.html', error="Пожалуйста, заполните все поля")

    conn, cur = db_connect()

    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT * FROM users WHERE login=%s;", (login,))
    else:
        cur.execute("SELECT * FROM users WHERE login=?;", (login,))
    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return render_template('rgz/login.html', error='Логин или пароль неверны')

    if not check_password_hash(user['password'], password):
        db_close(conn, cur)
        return render_template('rgz/login.html', error='Логин или пароль неверны')

    session['login'] = login
    session['user_name'] = user['user_name']

    db_close(conn, cur)
    return render_template('rgz/rgzok.html', login=login)

@rgz.route('/lab7/rest-api/products/', methods=['GET'])
def get_products():
    return jsonify(products)

@rgz.route('/lab7/rest-api/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((p for p in products if p['id'] == id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Товар не найден'}), 404

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'login' not in session:
            return redirect('/rgz/login')
        return f(*args, **kwargs)
    return decorated_function

@rgz.route('/rgz/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.json.get('product_id')
    if not product_id:
        return jsonify({'error': 'Product ID is required'}), 400

    if 'cart' not in session:
        session['cart'] = {}

    if product_id in session['cart']:
        session['cart'][product_id] += 1
    else:
        session['cart'][product_id] = 1

    session.modified = True
    return jsonify({'message': 'Товар добавлен в корзину', 'cart': session['cart']})

@rgz.route('/rgz/remove_from_cart', methods=['POST'])
def remove_from_cart():
    product_id = request.json.get('product_id')
    if not product_id:
        return jsonify({'error': 'Product ID is required'}), 400

    if 'cart' in session and product_id in session['cart']:
        del session['cart'][product_id]
        session.modified = True
        return jsonify({'message': 'Товар удален', 'cart': session['cart']})
    else:
        return jsonify({'error': 'Product not found in cart'}), 404

@rgz.route('/rgz/cart', methods=['GET'])
def view_cart():
    if 'cart' not in session:
        session['cart'] = {}


    cart_products = [p for p in products if str(p['id']) in session['cart']]
    total_price = sum(p['price'] * session['cart'][str(p['id'])] for p in cart_products)
    return render_template('rgz/cart.html', cart_products=cart_products, total_price=total_price)

@rgz.route('/rgz/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'GET':
        return render_template('rgz/checkout.html')

    if 'cart' in session:
        session.pop('cart')
        return render_template('rgz/checkout_success.html')
    else:
        return render_template('rgz/checkout.html', error="Корзина пуста")