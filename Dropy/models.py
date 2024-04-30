from django.db import models
from datetime import date, timedelta


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
    Zdjęcia = models.ImageField(upload_to='drops_images/')

    def __str__(self):
        return self.Tytuł

    @property
    def Dni_do(self):
        dzisiaj = date.today()
        dni_do = self.Data - dzisiaj
        dni_do_skrócone = str(dni_do).split('day', 1)[0]
        if self.Data < dzisiaj:
            dni_do_skrócone = "Drop zakończony"
        elif self.Data == dzisiaj:
            dni_do_skrócone = "Drop dzisiaj"
        elif self.Data == dzisiaj + timedelta(days=1):
            dni_do_skrócone = "Drop jutro"
        elif dzisiaj + timedelta(days=2) <= self.Data <= dzisiaj + timedelta(days=4):
            dni_do_skrócone = "Do dropu pozostały " + dni_do_skrócone + "dni"
        elif self.Data >= dzisiaj + timedelta(days=5):
            dni_do_skrócone = "Do dropu pozostało " + dni_do_skrócone + "dni"

        return dni_do_skrócone
