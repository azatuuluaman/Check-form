from django.core.validators import validate_email, RegexValidator
from django.db import models
from django import forms 


class Template(models.Model):
    name = models.CharField(max_length=50, verbose_name='Template name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'


class Field(models.Model):
    template = models.ForeignKey(Template, related_name='Example', verbose_name="Template", on_delete=models.CASCADE)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phoneRegex], max_length=16, unique=True)
    date = models.DateField()
    text = models.TextField(max_length=254)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not validate_email(email, verify=True):
            raise forms.ValidationError("Invalid email")
        return email

    # def __str__(self):
    #     return self.text

