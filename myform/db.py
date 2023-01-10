from django.shortcuts import render
from tinydb import TinyDB, Query

db = TinyDB('db.json')

User = Query()


def insert_db():
    """ Добавление данных в БД"""
    db.insert({
        "name": "Khabib",
        "email": "Khabib@mail.ru",
        "phone": "+71231231215",
        "date": "15.15.1518",
        "text": "Big text for something about somebody",
    })


def search_db(name, email, phone):
    """ Поиск вводимых данных в базе данных"""
    results = db.search(User.name == name)
    print(results)
    if User.filter(name=name).exists():
        print()


def list_db(request):
    """ Вывод искомых данных"""
    user_name = request.POST['name']
    lead_email = request.POST.get['email', False]
    phone = request.POST['phone']

    return render(request, 'myform/post.html', {'name': user_name,
                                                'email': lead_email,
                                                'phone': phone})

