from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    Nazwa = models.CharField(max_length=10)

    def __str__(self):
        return self.Nazwa


class Kategoria(models.Model):
    Nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.Nazwa


class Temat(models.Model):
    Autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Tytuł = models.CharField(max_length=255)
    Kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    Opis = models.TextField()
    Dodano = models.DateTimeField(auto_now_add=True)
    Status = models.ForeignKey(Status, default=1, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Tytuł + " | " + str(self.Kategoria)


class Komentarz(models.Model):
    Temat = models.ForeignKey(Temat, related_name="komentarze", on_delete=models.CASCADE)
    Autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Tekst = models.TextField(max_length=255)
    Dodano = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Temat) + " | " + "Autor: " + str(self.Autor) + " | " + str(self.Dodano)
