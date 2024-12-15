from flask import Flask, redirect, render_template, session
import os
app = Flask(__name__)

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретный-секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)


@app.route("/menu")
def menu():
    return render_template('menu.html')

