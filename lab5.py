from flask import Blueprint, render_template, request, session
import psycopg2
from psycopg2.extras import RealDictCursor
lab5 = Blueprint('lab5',__name__)

@lab5.route('/lab5/')
def lab_5():
    return render_template('lab5/lab5.html', login = session.get('login'))

def db_connect():
    conn = psycopg2.connect(
    host='127.0.0.1',      
    database='oparina_sofya_knowledge_base',  
    user='oparina_sofya_knowledge_base',        
    password='4321' 
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()


@lab5.route('/lab5/register', methods = ['GET', 'POST'])
def register_5():
    if request.method == 'GET':
        return render_template('lab5/register.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not (login and password): 
        return render_template('lab5/register.html', error="Пожалуйста, заполните все поля")


    conn, cur = db_connect()

    cur.execute("SELECT login FROM users WHERE login=%s;", (login,))

    if cur.fetchone():
        db_close(conn, cur)
        return render_template('lab5/register.html', error="Такой пользователь уже существует")


    cur.execute("INSERT INTO users (login, password) VALUES (%s, %s);", (login, password))

    db_close(conn, cur)

    return render_template('lab5/success.html', login=login)
    


@lab5.route('/lab5/login', methods=['GET', 'POST'])
def login_5():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login and password): 
        return render_template('lab5/login.html', error="Пожалуйста, заполните все поля")
    
    conn, cur = db_connect()

    cur.execute("SELECT * FROM users WHERE login=%s;", (login,))
    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return render_template('lab5/login.html', error = 'Логин или пароль неверны')
    
    if user['password'] != password:
        db_close(conn, cur)
        return render_template('lab5/login.html', error = 'Логин или пароль неверны')

    session['login'] = login   
    db_close(conn, cur)
    return render_template('lab5/success_login.html', login=login)


# @lab5.route('/lab5/create')
# def create():
