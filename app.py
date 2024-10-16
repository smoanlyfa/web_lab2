from flask import Flask, redirect
app = Flask(__name__)
from lab1 import lab1



app = Flask(__name__)
app.register_blueprint(lab1)



@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)


@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ ФБ Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>
            <li><a href = "http://127.0.0.1:5000/lab1">Первая лабораторная></a><li>
            <li><a href = "http://127.0.0.1:5000/lab2">Вторая лабораторная></a><li>
        </main>

        <footer>
            &copy; Опарина Софья, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""


@lab2.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@lab2.route('/lab2/dogs/')
def dogs():
    return render_template('dogs.html')