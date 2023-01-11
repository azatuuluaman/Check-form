from django.http import JsonResponse
from django.shortcuts import render

from myform.db import search_db
from myform.models import Template, Field


class template_view():
    def post(self, request):
        form = type_form(request.GET)
        for one, two in form.items():
            three = Field.object.filter(name_field=one, type_field=two)
            print(three.values_list())

        return JsonResponse(form)


def post_request(request):
    return render(request, 'myform/form_page.html', {})


def post_list(request):
    """ Вывод значений"""
    user_name = request.POST['name']

    search_db(user_name)

    return render(request, 'myform/post.html', {'name': user_name})