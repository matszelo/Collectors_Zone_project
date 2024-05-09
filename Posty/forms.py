from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('Tytuł', 'Kategoria', 'Opis', 'Zdjęcia')

        widgets = {
            'Tytuł': forms.TextInput(attrs={'class': 'form-control'}),
            'Kategoria': forms.Select(attrs={'class': 'form-control'}),
            'Opis': forms.Textarea(attrs={'class': 'form-control'}),
        }