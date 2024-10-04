from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

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
        </main>

        <footer>
            &copy; Опарина Софья, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""


@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
    <head>
        <title>Опарина Софья Александровна, Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, Лабораторная работа 1
        </header>

        <h2>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов 
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так 
            называемых микрофреймворков — минималистичных каркасов 
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </h2>
        <li><a href = "http://127.0.0.1:5000/menu">Меню></a><li>
        <h2>
        Реализованные роуты
        </h2>
            <li><a href = "http://127.0.0.1:5000/lab1/student">Студент></a><li>
            <li><a href = "http://127.0.0.1:5000/lab1/python">Питон></a><li>
            <li><a href = "http://127.0.0.1:5000/lab1/mango">Манго></a><li>
        <footer>
            &copy; Опарина Софья, ФБИ-23, 3 курс, 2024
        </footer>
        <link rel='stylesheet' href ="'''+url_for('static', filename = 'lab1.css')+'''">
    </body>
</html>
'''
@app.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Дуб</h1>
        <img src="'''+url_for('static', filename = 'oak.jpg')+'''">
        <link rel='stylesheet' href ="'''+url_for('static', filename = 'lab1.css')+'''">
    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <head>
        <title>Студент</title>
    </head>
    <body>
        <header>
            НГТУ, Лабораторная работа 1
        </header>
        <h1>
        Опарина Софья Александровна
        </h1>
        <img src="'''+url_for('static', filename = 'logo.png')+'''" width = "300" height ="300">
        <link rel='stylesheet' href ="'''+url_for('static', filename = 'lab1.css')+'''">
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!doctype html>
<html>
    <body>
        <header>
            НГТУ, Лабораторная работа 1
        </header>
        <h1>
            Python
        </h1>
        <h2>
            <p>
                Python — мультипарадигмальный высокоуровневый язык программирования общего назначения с динамической строгой 
                типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, 
                читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. Язык является полностью 
                объектно-ориентированным в том плане, что всё является объектами. 
            </p>
            <p>  
                Необычной особенностью языка является выделение блоков кода 
                отступами. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации. 
                Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов. Недостатками языка являются зачастую 
                более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, 
                написанным на компилируемых языках, таких как C или C++.
            </p>
        </h2>
        <img src="'''+url_for('static', filename = 'python.png')+'''" left = "50%" width = "300" height ="300" >
        <link rel='stylesheet' href ="'''+url_for('static', filename = 'lab1.css')+'''">
    </body>
</html>
'''

@app.route("/lab1/mango")
def mango():
    return '''
<!doctype html>
<html>
    <body>
        <header>
            НГТУ, Лабораторная работа 1
        </header>
        <h1>
            Манго
        </h1>
        <h2>
            <p>
            Ма́нго — плоды растений рода Манго (Mangifera) семейства Анакардиевые (Сумаховые).
            </p>
            <p>
                Вид Манго индийское (Mangifera indica) имеет большое сельскохозяйственное значение. В 2009 году в 
                сельском хозяйстве по всему миру выращивается больше 300 сортов этого вида. (К 1969 году было 
                известно около 200 сортов) Один из крупнейших экспортёров этого вида манго — Индия. Плоды манго 
                индийского обладают волокнистой структурой и сладким вкусом, кожура окрашена в тона красного, зелёного 
                или жёлтого цветов, у мякоти цвет жёлтый или оранжевый.
            </p>
        </h2>
        <img src="'''+url_for('static', filename = 'mango.jfif')+'''"width = "300" height ="300">
        <link rel='stylesheet' href ="'''+url_for('static', filename = 'lab1.css')+'''">
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Софья Опарина'
    nlab = '2'
    group = 'ФБИ-23'
    course = '3'
    return render_template('example.html', name=name, nlab=nlab, group=group, course=course)