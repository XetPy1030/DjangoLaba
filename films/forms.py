from django import forms
from .models import Category


def get_choices():
    return [[i.pk, i.name] for i in Category.objects.all()]


class FilmForm(forms.Form):
    name = forms.CharField(label='Имя фильма')
    category = forms.ChoiceField(label='Категория', choices=get_choices())
    release_date = forms.DateField(label='Дата выпуска')
    actors = forms.CharField(label='Актёры')
    show_date = forms.CharField(label='Дата показа')
    