from flask import Blueprint, render_template
lab2 = Blueprint('lab2',__name__)

@lab2.route('/lab2/')
def lab_2():
    return render_template('lab2/lab2.html')

@lab2.route('/lab2/example/')
def example():
    return render_template('lab2/example.html')


@lab2.route('/lab2/dogs/')
def dogs():
    return render_template('lab2/dogs.html')

