from flask import Blueprint, render_template, request, make_response, redirect, session, url_for
lab7 = Blueprint('lab7',__name__)

@lab7.route('/lab7/')
def lab_7():
    return render_template('lab7/lab7.html')