from flask import Blueprint, render_template, request, make_response, redirect
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