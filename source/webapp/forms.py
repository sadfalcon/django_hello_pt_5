from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, label='Заголовок')
    text = forms.CharField(max_length=3000, required=True, label='Текст', widget=forms.Textarea)
    author = forms.CharField(max_length=40, required=True, initial='Unknown', label='Автор')
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='Модерация')
    publish_at = forms.DateTimeField(required=False, label='Время публикации',
                                     input_formats=['%Y-%m-%d', BROWSER_DATETIME_FORMAT,
                                                    '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
                                                    '%Y-%m-%d %H:%M:%S'],
                                     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    # для полей типа DateField
    # publish_at = forms.DateField(..., widget=forms.DateInput(attrs={'type': 'date'}))
