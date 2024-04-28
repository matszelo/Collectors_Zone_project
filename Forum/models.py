from django.db import models
from django.contrib.auth.models import User


class Kategoria(models.Model):
    Nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.Nazwa


class Temat(models.Model):
    Autor = models.ForeignKey(User, on_delete=models.CASCADE)
    Tytuł = models.CharField(max_length=255)
    Kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    Opis = models.TextField()
    Dodano = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Tytuł


class Komentarz(models.Model):
    Temat = models.ForeignKey(Temat, related_name="komentarze", on_delete=models.CASCADE)
    Autor = models.ForeignKey(User, on_delete=models.CASCADE)
    Tekst = models.TextField()
    Dodano = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Temat.Tytuł
