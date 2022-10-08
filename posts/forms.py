""" forms.py """
""" forms.py """
from django import forms
from posts.models import POST_TYPE_CHOICES


class PostForm(forms.Form):
    title = forms.CharField(
        label="Название",
        max_length=100,
        min_length=8
    )
    description = forms.CharField(
        label="Описание",
        widget=forms.Textarea()
    )
    stars = forms.IntegerField(
        label="Сколько звезд",
        max_value=5,
        min_value=0
    )
    type = forms.ChoiceField(
        label="Выберите тип поста",
        choices=POST_TYPE_CHOICES
    )


class Commentform(forms.Form):
    author = forms.CharField(
        label='Автор',
        max_length=100,
        min_length=5
    )
    text = forms.CharField(
        widget=forms.Textarea(),
        label="Описание",
        max_length=100,
        min_length=5
    )