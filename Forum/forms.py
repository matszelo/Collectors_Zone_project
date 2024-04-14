from django import forms
from django.forms import ModelForm
from .models import Temat, Komentarz


class TopicForm(ModelForm):
    class Meta:
        model = Temat
        fields = ('Tytuł', 'Kategoria', 'Opis')

class CommentForm(ModelForm):
    Tekst = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
        ),
    )

    class Meta:
        model = Komentarz
        fields = ('Tekst',)
