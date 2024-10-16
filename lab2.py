from flask import Blueprint, render_template
lab2 = Blueprint('lab2',__name__)

@lab2.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@lab2.route('/lab2/dogs/')
def dogs():
    return render_template('dogs.html')