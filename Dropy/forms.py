from django import forms
from django.forms import ModelForm
from Dropy.models import Drop


class DropForm(ModelForm):
    class Meta:
        model = Drop
        fields = ('Tytuł', 'Typ', 'Strona', 'Cena', 'Data', 'Godzina', 'Zdjęcia')

        widgets = {
            'Tytuł': forms.TextInput(attrs={'class': 'form-control'}),
            'Typ': forms.Select(attrs={'class': 'form-control'}),
            'Strona': forms.TextInput(attrs={'class': 'form-control'}),
            'Cena': forms.TextInput(attrs={'class': 'form-control'}),
            'Data': forms.DateInput(attrs={'class': 'form-control'}, format='%d.%m.%Y'),
            'Godzina': forms.TimeInput(attrs={'class': 'form-control'}, format='%H:%M'),
        }
