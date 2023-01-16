from django.shortcuts import render
from myform.db import check_in_db


def post_request(request):
    return render(request, 'myform/form_page.html', {})


def post_list(request):
    """ Вывод значений
    Если находит искомое, то показывает на мониторе.
    Если нет такого, то показывает, что нет такого"""
    user_name = request.POST['name']
    if check_in_db(user_name) == 'Object is not in db':
        return render(request, 'myform/post.html', {'name': 'нет такого'})
    else:
        return render(request, 'myform/post.html', {'name': user_name})
