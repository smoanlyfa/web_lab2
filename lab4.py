from flask import Blueprint, render_template, request, make_response, redirect, session
lab4 = Blueprint('lab4',__name__)

@lab4.route('/lab4/')
def lab_4():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods=['POST'])
def div():
    
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')

    x1 = int(x1)
    x2 = int(x2)

    try:
        result1 = x1 / x2  # Деление
    except ZeroDivisionError:
        result1 = 'Ошибка: деление на ноль'

    result2 = x1 + x2  
    result3 = x1 * x2  
    result4 = x1 - x2   
    result5 = x1 ** x2  

    return render_template('lab4/div.html', 
                           x1=x1, 
                           x2=x2, 
                           result1=result1, 
                           result2=result2, 
                           result3=result3, 
                           result4=result4, 
                           result5=result5)


tree_count = 0
max_count = 10
@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')

    if operation == 'cut':
        if tree_count > 0:
            tree_count -= 1
    elif operation == 'plant':
        if tree_count < max_count:
            tree_count += 1

    return redirect('/lab4/tree')


users = [
    {'login': 'alex', 'password': '123', 'name': 'Александр Петров', 'gender': 'мужской'},
    {'login': 'bob', 'password': '321', 'name': 'Боб Марли', 'gender': 'мужской'},
    {'login': 'yan', 'password': '456', 'name': 'Яна Смирнова', 'gender': 'женский'},
    {'login': 'erik', 'password': '654', 'name': 'Эрик Солнечный', 'gender': 'мужской'},
    {'login': 'job', 'password': '890', 'name': 'Джобс Уолтер', 'gender': 'мужской'},
    {'login': 'klark', 'password': '098', 'name': 'Кларк Кент', 'gender': 'женский'},
]
@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    name=''
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            name = next((user['name'] for user in users if user['login'] == login), login)
        else:
            authorized = False
            login = ''
        return render_template('lab4/login.html', authorized=authorized, login=login, name=name)

    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)

    if not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    
    for user in users:  
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4/login')
    
    error = 'Неверный логин или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, name=name)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')  

@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    message = ''
    temperature = None

    if request.method == 'POST':
        try:
            temperature = float(request.form.get('temperature'))
            if temperature is None:
                message = 'Ошибка: не задана температура'
            elif temperature < -12:
                message = 'Не удалось установить температуру — слишком низкое значение'
            elif temperature > -1:
                message = 'Не удалось установить температуру — слишком высокое значение'
            elif -12 <= temperature <= -9:
                message = f'Установлена температура: {temperature}°С ❄️❄️❄️' 
            elif -8 <= temperature <= -5:
                message = f'Установлена температура: {temperature}°С ❄️❄️'
            elif -4 <= temperature <= -1:
                message = f'Установлена температура: {temperature}°С ❄️' 
        except ValueError:
            message = 'Ошибка: не задана температура'

    return render_template('lab4/fridge.html', message=message, temperature=temperature)

