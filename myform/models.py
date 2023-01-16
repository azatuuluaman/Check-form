from django.core.validators import RegexValidator
from django.db import models


class Template(models.Model):
    name_field = models.CharField(max_length=256, verbose_name='Name')
    email_field = models.EmailField(blank=True, null=True, verbose_name='Email')
    phone_field = models.CharField(validators=[RegexValidator], max_length=16, unique=True, verbose_name='Phone number')
    date_field = models.DateField(blank=True, null=True, verbose_name='Birthday date')
    text_field = models.TextField(max_length=2000, verbose_name='Text')

    def __str__(self):
        return self.name_field

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'
