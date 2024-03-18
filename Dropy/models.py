from django.db import models
from datetime import date


class Typ(models.Model):
    Nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.Nazwa


class Drop(models.Model):
    Tytuł = models.CharField(max_length=255)
    Typ = models.ForeignKey(Typ, on_delete=models.CASCADE)
    Strona = models.CharField(max_length=255)
    Cena = models.CharField(max_length=255)
    Data = models.DateField()
    Godzina = models.TimeField()
    Zdjęcia = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.Tytuł

    @property
    def Dni_do(self):
        dzisiaj = date.today()
        dni_do = self.Data - dzisiaj
        dni_do_skrócone = str(dni_do).split('days', 1)[0]
        if self.Data == dzisiaj:
            dni_do_skrócone = "Drop dzisiaj"
        elif self.Data < dzisiaj:
            dni_do_skrócone = "Drop zakończony"
        elif self.Data > dzisiaj:
            dni_do_skrócone = "Do dropu pozostało " + dni_do_skrócone + "dni"

        return dni_do_skrócone
