from django.shortcuts import render, HttpResponse
from . models import * # naimportovanie všetkých modelov z models.py v tomto priečinku

def index(request):
    studenti = Student.objects.all()
    ucitelia = Ucitel.objects.all()
    triedy = Trieda.objects.all()
    return render(request, "skola/index.html", {"studenti":studenti, "ucitelia":ucitelia, "triedy":triedy})

def list_students(request):
    studenti = Student.objects.all()
    return render(request, "skola/index.html", {"studenti":studenti})    

def list_teachers(request):
    ucitelia = Ucitel.objects.all()
    return render(request, "skola/index.html", {"ucitelia":ucitelia})

def list_triedy(request):
    triedy = Trieda.objects.all()
    return render(request, "skola/index.html", {"triedy":triedy})    