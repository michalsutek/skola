from django.contrib import admin
from .models import Student # naimportovanie modelu Student do admin.py

admin.site.register(Student)
