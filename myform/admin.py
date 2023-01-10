from django.contrib import admin
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Template, Field

admin.site.register(Template)
admin.site.register(Field)


# class ContactForm(forms.ModelForm):
#     class Meta:
#         widgets = {                          # Here
#             'phone': PhoneNumberPrefixWidget(initial='E164'),
#         }