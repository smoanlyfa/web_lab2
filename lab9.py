from flask import Flask, Blueprint, render_template, request, redirect, session

lab9 = Blueprint('lab9',__name__)


@lab9.route('/lab9/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect('/lab9/age')
    return render_template('lab9/lab9.html')

@lab9.route('/lab9/age', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        session['age'] = request.form['age']
        return redirect('/lab9/gender')
    return render_template('lab9/age.html')


@lab9.route('/lab9/gender', methods=['GET', 'POST'])
def gender():
    if request.method == 'POST':
        session['gender'] = request.form['gender']
        return redirect('/lab9/preference1')
    return render_template('lab9/gender.html')

@lab9.route('/lab9/preference1', methods=['GET', 'POST'])
def preference1():
    if request.method == 'POST':
        session['preference1'] = request.form['preference1']
        return redirect('/lab9/preference2')
    return render_template('lab9/preference1.html')

@lab9.route('/lab9/preference2', methods=['GET', 'POST'])
def preference2():
    if request.method == 'POST':
        session['preference2'] = request.form['preference2']
        return redirect('/lab9/result')
    return render_template('lab9/preference2.html')


@lab9.route('/lab9/result')
def result():
    if 'username' not in session:
        return redirect('/lab9')
    return render_template('lab9/result.html', session=session)

@lab9.route('/lab9/reset')
def reset():
    session.clear()
    return redirect('/lab9')