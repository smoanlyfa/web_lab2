from flask import Blueprint, render_template, request
import psycopg2
lab5 = Blueprint('lab5',__name__)

@lab5.route('/lab5/')
def lab_5():
    return render_template('lab5/lab5.html')

@lab5.route('/lab5/register', methods = ['GET', 'POST'])
def register_5():
    if request.method == 'GET':
        return render_template('lab5/register.html')

    login = request.form.get('login')
    password = request.form.get('password')

    if not (login and password): 
        return render_template('lab5/register.html', error="Пожалуйста, заполните все поля")


    conn = psycopg2.connect(
        host='127.0.0.1',      
        database='oparina_sofya_knowledge_base',  
        user='oparina_sofya_knowledge_base',        
        password='4321' 
    )
    cur = conn.cursor()

    cur.execute("SELECT login FROM users WHERE login=%s;", (login,))
    
    if cur.fetchone():
        cur.close()
        conn.close()
        return render_template('lab5/register.html', error="Такой пользователь уже существует")


    cur.execute("INSERT INTO users (login, password) VALUES (%s, %s);", (login, password))
    conn.commit()
    cur.close()
    conn.close()

    return render_template('lab5/success.html', login=login)
    


# @lab5.route('/lab5/list')
# def list_5():

# @lab5.route('/lab5/create')
# def create():
