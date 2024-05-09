from django.db import models


class Kategoria(models.Model):
    Nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.Nazwa


class Post(models.Model):
    Tytuł = models.CharField(max_length=255)
    Kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    Opis = models.TextField()
    Zdjęcia = models.ImageField(null=True, blank=True, upload_to='post_images/')

    def __str__(self):
        return self.Tytuł
