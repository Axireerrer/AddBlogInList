from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Логин...',
                                                             'class': 'form-auth'}), label='ЛОГИН', )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль...',
                                                                 'class': 'form-auth'}), label='ПАРОЛЬ')

  


class RegisterForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input',
                                                         'placeholder': 'Имя...'}), label='Имя')

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                 'placeholder': 'Пароль...'}), label='Пароль')

    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                   'placeholder': 'Повтор пароля...'}), label='Повтор пароля')

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'password_2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input','placeholder': 'Логин...'}),

            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Фамилия...'}),

            'email': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'E-mail...'}),
        }
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'E-mail',
        }

    def clean_password_2(self):
        cred = self.cleaned_data
        if cred['password'] != cred['password_2']:
            raise forms.ValidationError("Пароли не совпадают")
        return cred['password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Почта уже существует")
        return email

