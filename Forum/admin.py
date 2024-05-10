from django.contrib import admin
from .models import Temat, Kategoria, Komentarz, Status

admin.site.register(Temat)
admin.site.register(Kategoria)
admin.site.register(Komentarz)
admin.site.register(Status)

