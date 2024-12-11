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
    for pismeno in ['A', 'B', 'C', 'D']:
        Trieda.objects.create(nazov=f"{rocnik}.{pismeno}")

for meno in ["Ján", "Adam", "Jozef", "Tomáš"]:
    for priezvisko in ["Mrkvička", "Šarlina", "Šutek", "Trnka"]:
        Student.objects.create(meno=meno, priezvisko=priezvisko)

for meno in ["Ján", "Adam", "Jozef", "Tomáš"]:
    for priezvisko in ["Mrkvička", "Šarlina", "Šutek", "Trnka"]:
        titul = random.choice(["Mgr.", "Ing.", "PhDr."])
        Ucitel.objects.create(titul=titul, meno=meno, priezvisko=priezvisko)
