from django.contrib import admin
from .models import Student, Ucitel, Trieda, Kruzok # naimportovanie modelu Student do admin.py

admin.site.register(Student)
admin.site.register(Ucitel)
admin.site.register(Trieda)
admin.site.register(Kruzok)