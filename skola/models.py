from django.db import models


class Trieda(models.Model):
    nazov = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nazov}"
    
    class Meta:
        verbose_name = "Trieda"
        verbose_name_plural = "Triedy"
        ordering = ["nazov"]



class Ucitel(models.Model):
    titul = models.CharField(max_length=10)
    meno = models.CharField(max_length=20) # textové pole
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.trieda:
            return f"{self.titul} {self.meno} {self.priezvisko}, {self.trieda}"
        else:
            return f"{self.titul} {self.meno} {self.priezvisko}"
    
    class Meta:
        verbose_name = "Učiteľ"
        verbose_name_plural = "Učitelia"
        ordering = ["priezvisko"]



class Kruzok(models.Model):
    nazov = models.CharField(max_length=100)
    skratka = models.CharField(max_length=10)
    ucitel = models.ForeignKey(Ucitel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nazov}"

    class Meta:
        ordering = ["nazov"]
        verbose_name = "Krúžok"
        verbose_name_plural = "Krúžky"



class Student(models.Model):
    meno = models.CharField(max_length=20) # textové pole
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
    kruzok = models.ManyToManyField(Kruzok, blank=True)

    def __str__(self):
        if self.trieda:
            return f"{self.meno} {self.priezvisko}, {self.trieda}"
        else:
            return f"{self.meno} {self.priezvisko}"
    
    class Meta:
        verbose_name = "Študent"
        verbose_name_plural = "Študenti"
        ordering = ["priezvisko"]

    # class Meta je na zobrazovanie slovenských názvov