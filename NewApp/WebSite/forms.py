from django import forms
from .models import FamousPerson, CategoryPerson


class FamousPersonForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=CategoryPerson.objects.all(),
                                      label='Категория', empty_label='Не выбрано')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input', 'cols': 5, 'rows': 2}),
                                  label='Описание')
    age = forms.IntegerField(required=False, label='Возраст',
                             widget=forms.TextInput(attrs={'placeholder': 'Возраст...', 'class': 'form-input'}))

    class Meta:
        model = FamousPerson
        fields = ['name', 'surname', 'age', 'description', 'slug', 'category', 'image']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'age': 'Возраст',
            'description': 'Описание',
            'slug': 'URL',
            'category': 'Категория',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя...', 'class': 'form-input'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Фамилия...', 'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'placeholder': 'URL...', 'class': 'form-input'}),
        }