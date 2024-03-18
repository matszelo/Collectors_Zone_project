from django import forms
from .models import Drop


class DropForm(forms.ModelForm):
    class Meta:
        model = Drop
        fields = ('Tytuł','Typ', 'Strona', 'Cena', 'Data', 'Godzina', 'Zdjęcia')

    Data = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'), input_formats=('%d.%m.%Y',)
    )

    Godzina = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M'), input_formats=('%H:%M',)
    )
