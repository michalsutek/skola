from django.shortcuts import render, HttpResponse
from . models import * # naimportovanie všetkých modelov z models.py v tomto priečinku

def index(request):
    studenti = Student.objects.all()
    ucitelia = Ucitel.objects.all()
    triedy = Trieda.objects.all()
    kruzky = Kruzok.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {"studenti":studenti, "ucitelia":ucitelia, "triedy":triedy, "kruzky":kruzky})

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

def detail_student(request, pk):
    student = Student.objects.get(pk=pk)
    kruzky = Kruzok.objects.filter(student=student)
    return render(request, "skola/detail_student.html", {"student":student, "kruzky":kruzky})

def vypis_kruzky(request):
    kruzky = Kruzok.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {"kruzky":kruzky})

def vypis_kruzok(request, kruzok):
    kruzok = Kruzok.objects.get(skratka=kruzok)
    studenti = Student.objects.filter(kruzok=kruzok.pk).order_by("priezvisko")
    # ucitel = Ucitel.objects.get(pk=kruzok.ucitel_id)
    ucitel = kruzok.ucitel
    # ucitel = f"{ucitel.titul} {ucitel.meno} {ucitel.priezvisko}"
    return render(request, "skola/vypis_kruzok.html", {'studenti':studenti,'kruzok':kruzok,'ucitel':ucitel})