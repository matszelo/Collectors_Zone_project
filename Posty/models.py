from django.db import models


class Kategoria(models.Model):
    Nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.Nazwa


class Post(models.Model):
    Tytuł = models.CharField(max_length=255)
    Kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    Opis = models.TextField()

    def __str__(self):
        return self.Tytuł
