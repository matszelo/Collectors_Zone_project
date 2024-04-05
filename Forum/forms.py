from django import forms
from django.forms import ModelForm
from .models import Temat


class TopicForm(ModelForm):
    class Meta:
        model = Temat
        fields = ('Tytuł', 'Kategoria', 'Opis')