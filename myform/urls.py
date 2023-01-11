from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post'),
    path('get_form/', views.post_request, name='post_request'),
    path('template_view/', views.template_view, name='template_view')
]