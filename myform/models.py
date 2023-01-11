from django.db import models


class Template(models.Model):
    name = models.CharField(max_length=50, verbose_name='Template name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'


class Field(models.Model):
    class Type:
        choices = (
            ('email', "email"),
            ('date', "date"),
            ('phone', "phone"),
            ('text', "text"),
        )

    template = models.ForeignKey(Template, related_name='Example', verbose_name="Template", on_delete=models.CASCADE)
    type_field = models.CharField(max_length=5, choices=Type.choices, verbose_name='Field type')
    name_field = models.CharField(max_length=256, verbose_name='Field name')

# def clean_email(self):
#     name_field = models.EmailField(max_length=70, blank=True, null=True, unique=True)
#     email = self.cleaned_data.get("email")
#     if not validate_email(email, verify=True):
#         raise forms.ValidationError("Invalid email")
#     return email

# if type_field == 'email':
#     name_field = models.EmailField(max_length=70, blank=True, null=True, unique=True)
#
# def clean_email(self):
#     email = self.cleaned_data.get("email")
#     if not validate_email(email, verify=True):
#         raise forms.ValidationError("Invalid email")
#     return email

# if type_field == 'date':
#
# phoneRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
# phone = models.CharField(validators=[phoneRegex], max_length=16, unique=True)
# date = models.DateField()
# text = models.TextField(max_length=254)

# def __str__(self):
#     return self.text
