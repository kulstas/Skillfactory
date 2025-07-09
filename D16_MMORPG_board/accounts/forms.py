from django.utils.crypto import get_random_string
import random
from django.contrib.auth.models import Group
from django import forms
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from D16_MMORPG_board.models import OneTimeCode
from django.core.mail import EmailMultiAlternatives
from django.core.mail import mail_managers, mail_admins
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from D16_MMORPG_board.models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        label='Username',
        error_messages={"required": "Необходимо указать Имя"},
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        label="Email",
        error_messages={"required": "Необходимо ввести действующий Email"},
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label='Пароль',
        error_messages={"required": "Пожалуйста, придумайте и введите пароль"},
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Повтор пароля',
        error_messages={"required": "Необходимо ввести пароль повторно"},
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = 'Укажите Username'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].help_text = 'Укажите Email'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = 'Укажите пароль'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = 'Укажите Username'

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email

    def send_activation_email(self, user):
        activation_code = random.randint(000000, 111111)
        OneTimeCode.objects.create(code=activation_code, user=user)
        mail_subject = "Регистрация на портале D16-MMORPG (активация)"
        message = render_to_string("accounts/email_activation.html", {
            'user': user.username,
            'code': activation_code,
        })
        email = EmailMessage(mail_subject, message, to=[user.email])
        email.send()


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Пароль'}))


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'user_avatar',
            'user_subscriber',
        ]


class CheckCode(forms.Form):
    code = forms.CharField(label="Укажите код", max_length=6)