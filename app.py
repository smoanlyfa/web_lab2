from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
<!doctype html>
<html>
    <head>
        <title>Опарина Софья Александровна, Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, Лабораторная работа 1
        </header>

        <h1>web-сервер на Flask</h1>

        <footer>
            &copy; Опарина Софья, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""
