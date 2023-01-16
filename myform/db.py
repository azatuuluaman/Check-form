from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from tinydb import TinyDB, Query

db = TinyDB('tinydb.json')

User = Query()
test_db = {
    "User1": {
        "date_field": "User_phone1",
        "phone_field": "phone1",
        "email_field": "email1",
        "text_field": "text1",
    },
    "User2": {
        "date_field": "User_phone2",
        "phone_field": "phone2",
        "email_field": "email2",
        "text_field": "text2",
    },
    "User3": {
        "date_field": "User_phone3",
        "phone_field": "phone3",
        "email_field": "email3",
        "text_field": "text3",
    }
}


# def list_db(request):
#     """ Вывод искомых данных"""
#     user_name = request.POST['name']
#     lead_email = request.POST.get['email', False]
#     phone = request.POST['phone']
#
#     return render(request, 'myform/post.html', {'name': user_name,
#                                                 'email': lead_email,
#                                                 'phone': phone})


def check_in_db(obj: str):
    """
    Проверка наличия объекта в БД. Проверяет только одно значение. УБрать остальные две в   html
    """
    for k, v in test_db.items():
        if obj in v.values():
            return k
        elif obj not in v.values():
            return 'Object is not in db'

