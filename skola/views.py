from django.shortcuts import render, HttpResponse
from . models import * # naimportovanie všetkých modelov z models.py v tomto priečinku

def index(request):
    studenti = Student.objects.all()
    return HttpResponse(studenti)
