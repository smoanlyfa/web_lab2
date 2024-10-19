from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab_3():
    name = request.cookies.get('name')
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'green')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('lab3/args.get1.html', user = user, age = age, sex = sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black tea':
        price = 80
    else:
        price = 90

    if request.args.get('milk') == 'on':
        price += 20
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    return render_template('lab3/success.html')


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    background = request.args.get('background')
    font = request.args.get('font')
    style = request.args.get('style')

    if color:
        resp = make_response(redirect('lab3/settings.html'))
        resp.set_cookie('color', color)
        return resp
    
    if background:
        resp = make_response(redirect('lab3/settings.html'))
        resp.set_cookie('background', background)
        return resp
    
    if font:
        resp = make_response(redirect('lab3/settings.html'))
        resp.set_cookie('font', font)
        return resp
    
    if style:
        resp = make_response(redirect('lab3/settings.html'))
        resp.set_cookie('style', style)
        return resp
    
        
    color = request.cookies.get('color')
    resp = make_response(render_template('lab3/settings.html', color=color))
    

    background = request.cookies.get('background')
    resp = make_response(render_template('lab3/settings.html', background=background))
    

    font = request.cookies.get('font')
    resp = make_response(render_template('lab3/settings.html', font=font))
    

    style = request.cookies.get('style')
    resp = make_response(render_template('lab3/settings.html', style=style))
    return resp

@lab3.route('/lab3/tutu')
def tutu():
    return render_template("/lab3/tutu.html")

@lab3.route('/lab3/ticket')
def ticket():
    fio = request.args.get["fio"]
    sleeper = request.args.get["sleeper"]
    bedding = "yes" if "bedding" in request.args.get else "no"
    luggage = "yes" if "luggage" in request.args.get else "no"
    age = int(request.args.get["age"])
    departure = request.args.get["departure"]
    destination = request.args.get["destination"]
    date = request.args.get["date"]
    insurance = "yes" if "insurance" in request.args.get else "no"

    # Определение стоимости
    price = 1000 if age >= 18 else 700  # Взрослый или детский билет
    if sleeper in ["нижняя", "нижняя боковая"]:
        price += 100
    if bedding == "yes":
        price += 75
    if luggage == "yes":
        price += 250
    if insurance == "yes":
        price += 150

    ticket_type = "Детский билет" if age < 18 else "Взрослый билет"

    return render_template('lab3/ticket.html', fio=fio, sleeper=sleeper,
                           bedding=bedding, luggage=luggage, age=age,
                           departure=departure, destination=destination,
                           date=date, insurance=insurance, price=price,
                           ticket_type=ticket_type)

if __name__ == "__main__":
    lab3.run(debug=True)



