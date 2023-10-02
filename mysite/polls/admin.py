from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# show Choice model and question model
admin.site.register(Choice)
admin.site.register(Question)

