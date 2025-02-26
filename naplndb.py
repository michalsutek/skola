import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()

from skola.models import *
import random

Trieda.objects.all().delete() # vymaže všetky záznamy v tabulke tried
Student.objects.all().delete()
Ucitel.objects.all().delete()

# Trieda.objects.create(nazov=f"I.A") # vytvorí záznam v tabuľke tried

for rocnik in range(1,5):
    for pismeno in ['A', 'B', 'C']:
        Trieda.objects.create(nazov=f"{rocnik}.{pismeno}")


triedy = Trieda.objects.all()

fmena = open('mena.txt', 'r', encoding='utf-8')
mena = fmena.read().splitlines()

fpriezviska = open('priezviska.txt', 'r', encoding='utf-8')
priezviska = fpriezviska.read().splitlines()

pocet_tried = len(triedy)
for i in range(24):
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    titul = random.choice(["Mgr.", "Ing.", "PhDr.", "PeaDr.", ""])
    if i < pocet_tried:
        trieda = triedy[i]
        Ucitel.objects.create(titul=titul, meno=meno, priezvisko=priezvisko, trieda=trieda)
    else:
        Ucitel.objects.create(titul=titul, meno=meno, priezvisko=priezvisko)
    
for i in range(240):
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    trieda = random.choice(triedy)
    Student.objects.create(meno=meno, priezvisko=priezvisko, trieda=trieda)  