from flask import Blueprint, render_template, request, session, redirect, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path

rgz = Blueprint('rgz',__name__)

@rgz.route('/rgz/')
def lab_5():
    return render_template('rgz/rgz.html', login = session.get('login'), user_name = session.get('user_name'))

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

    # Проверка, что все поля заполнены
    if not (login and password and user_name and phone):
        return render_template('rgz/register.html', error="Пожалуйста, заполните все поля")

    conn, cur = db_connect()

    # Проверка, существует ли пользователь с таким логином
    if current_app.config['DB_TYPE'] == 'postgres':
        cur.execute("SELECT login FROM users WHERE login=%s;", (login,))
    else:
        cur.execute("SELECT login FROM users WHERE login=?;", (login,))

    if cur.fetchone():
        db_close(conn, cur)
        return render_template('rgz/register.html', error="Такой пользователь уже существует")

    # Хэширование пароля
    password_hash = generate_password_hash(password)

    # Добавление пользователя в базу данных
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
        return render_template('rgz/login.html', error = 'Логин или пароль неверны')
    
    if not check_password_hash(user['password'], password):
        db_close(conn, cur)
        return render_template('rgz/login.html', error = 'Логин или пароль неверны')

    session['login'] = login

    db_close(conn, cur)
    return render_template('rgz/rgzok.html', login=login)