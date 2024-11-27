from django.db import models

class Student(models.Model):
    meno = models.CharField(max_length=20) # textové pole
    priezvisko = models.CharField(max_length=20)
    trieda = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.meno} {self.priezvisko}, {self.trieda}"
