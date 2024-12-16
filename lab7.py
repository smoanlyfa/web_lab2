from flask import Blueprint, render_template, request, make_response, redirect, session, url_for

lab7 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def lab_7():
    return render_template('lab7/lab7.html')

films = [
    {
        "title": "City of Thieves",
        "title_ru": "Город воров",
        "year": 2010,
        "description": "В Бостоне каждый год происходит более 300 ограблений банков.\
        И большинство профессионалов, специализирующихся в этой области,\
        живут в округе под названием Чарльстон общей площадью одна квадратная миля. \
        Даг МакРэй — один из них. В отличие от большинства у Дага был шанс на успех, \
        шанс на то, чтобы не идти по криминальному пути своего отца. Однако вместо этого \
        он стал фактическим лидером группы безжалостных грабителей банков, которые гордятся \
        тем, что берут все, что хотят, и выходят сухими из воды."
    },
    {
        "title": "The Hangover",
        "title_ru": "Мальчишник в Вегасе",
        "year": 2009,
        "description": "Они мечтали устроить незабываемый мальчишник в Вегасе. \
        Но теперь им необходимо вспомнить, что именно произошло: что за ребенок \
        сидит в шкафу номера отеля? Как в ванную попал тигр? Почему у одного из них \
        нет зуба? И, самое главное, куда делся жених? То, что парни вытворяли на вечеринке, \
        не идет ни в какое сравнение с тем, что им придется сделать на трезвую голову, \
        когда они будут шаг за шагом восстанавливать события прошлой ночи."
    },
    {
        "title": "The Dark Knight",
        "title_ru": "Темный рыцарь",
        "year": 2008,
        "description": "Бэтмен поднимает ставки в войне с криминалом. \
        С помощью лейтенанта Джима Гордона и прокурора Харви Дента он \
        намерен очистить улицы Готэма от преступности. Сотрудничество \
        оказывается эффективным, но скоро они обнаружат себя посреди хаоса, \
        развязанного восходящим криминальным гением, известным напуганным горожанам \
        под именем Джокер."
    },
]


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if 0 <= id < len(films):
        return films[id]
    else:
        return ({'error': 'Фильм не найден'}), 404
    
@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if 0 <= id < len(films):
        del films[id]
        return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT']) 
def put_film(id):
    film = request.get_json()
    if 0 <= id < len(films):
        films[id] = film 
        return films[id]


@lab7.route('/lab7/rest-api/films/', methods=['POST']) 
def add_film():
    film = request.get_json()
    films.append(film)
    return '', 201
