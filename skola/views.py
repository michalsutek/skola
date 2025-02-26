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

def vypis_trieda(request, pk):
    trieda = Trieda.objects.get(pk=pk) # do premennej trieda priradí jeden objekt konkrétnej triedy (pk)
    studenti = Student.objects.filter(trieda=trieda).order_by("priezvisko")
    ucitel = Ucitel.objects.get(trieda=trieda)
    return render(request, "skola/vypis_trieda.html", {"trieda":trieda, "studenti":studenti, "ucitel":ucitel})