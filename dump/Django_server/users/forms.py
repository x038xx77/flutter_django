from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms.models import ModelForm
from users.models import Promocode
# from django.contrib.auth.forms import AuthenticationForm
# from django.forms.widgets import PasswordInput, TextInput
from django.utils.translation import gettext_lazy as _, ugettext_lazy

User = get_user_model()


class CreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=ugettext_lazy('Введите пароль'),
        widget=forms.PasswordInput(attrs={'placeholder': ugettext_lazy('поле для пароля')}))
    password2 = forms.CharField(
        label=_('Повторите пароль'),
        widget=forms.PasswordInput(attrs={'placeholder': ugettext_lazy('поле подтверждения')}))

    class Meta(UserCreationForm):
        model = User
        fields = (
            'first_name',
            'last_name',
            'birthday',
            'phone',
            'username',
            'email',
            'avatar',
            'password1',
            'password2',
            'code_word',
            'number_btc',
            'whatsapp',
            'telegram',)

        widgets = {

            'phone': forms.TextInput(
                attrs={
                    'class': 'input is-large',
                    'placeholder': ugettext_lazy('Контактный телефон, начиная c +7XXX... .')
                    }),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': ugettext_lazy('Имя')}),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': ugettext_lazy('Фамилия')
                    }),
            'avatar': forms.FileInput(
                attrs={
                    'class': 'file-input',
                    'placeholder': ugettext_lazy('фото аватар')
                    }),
            'birthday': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': ugettext_lazy('гггг-мм-дд')
                    }),
            'username': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': ugettext_lazy('Логин')
                    }),
            'email': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Email'
                    }),
            'code_word': forms.PasswordInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Code word'
                    }),
            'number_btc': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Number BTC'
                    }),
            'whatsapp': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'You whatsapp'
                    }),
            'telegram': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'You telegramm'
                    }),
        }

        labels = {
            'first_name': ugettext_lazy('Введите ваше имя'),
            'last_name': ugettext_lazy('Введите вашу фамилию'),
            'birthday': ugettext_lazy('Введите дату рождения'),
            'phone': ugettext_lazy('Введите номер телефона'),
            'username': ugettext_lazy('Введите username'),
            'email': ugettext_lazy('Введите E-mail'),
            'avatar': ugettext_lazy('Ваше фото-avatar'),
            'code_word': ugettext_lazy('Кодовое слово'),
            'number_btc': ugettext_lazy('Номер публичного кошелька BTC'),
            'whatsapp': ugettext_lazy('Ссылка на Ваш whatsapp'),
            'telegram': ugettext_lazy('Ссылка на Ваш telegram'),
            }

        error_messages = {
            'username': {
                'required': ugettext_lazy("Обязательное поле, введите логин пользователя")},
                }

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError(
                ugettext_lazy('Логин уже используется, измените на другой.'))
        return username


class UpdateUserForm(UserCreationForm):
    password1 = forms.CharField(
        label=ugettext_lazy('Введите пароль снова'),
        widget=forms.PasswordInput(attrs={'placeholder': ugettext_lazy('поле пароля')}))
    password2 = forms.CharField(
        label=ugettext_lazy('Повторите пароль снова'),
        widget=forms.PasswordInput(attrs={'placeholder': ugettext_lazy('поле подтверждения пароля')}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'birthday',
            'phone',
            'username',
            'email',
            'avatar',
            'code_word',
            'number_btc',
            'whatsapp',
            'telegram',)

        widgets = {

            'phone': forms.TextInput(
                attrs={
                    'class': 'input is-large',
                    'placeholder': ugettext_lazy('Контактный телефон, начиная c +7XXX... .')
                    }),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': ugettext_lazy('Имя')}),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': ugettext_lazy('Фамилия')
                    }),
            'avatar': forms.FileInput(
                attrs={
                    'class': 'input',
                    'placeholder': ugettext_lazy('фото аватар')
                    }),
            'birthday': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': ugettext_lazy('гггг-мм-дд')
                    }),
            'username': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': ugettext_lazy('Логин')
                    }),
            'email': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Email'
                    }),
            'code_word': forms.PasswordInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Code word'
                    }),
            'number_btc': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'Number BTC'
                    }),
            'whatsapp': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'You whatsapp'
                    }),
            'telegram': forms.TextInput(
                attrs={
                    'class': 'input',
                    'placeholder': 'You telegramm'
                    }),
        }

        labels = {
            'first_name': ugettext_lazy('Введите ваше имя'),
            'last_name': ugettext_lazy('Введите вашу фамилию'),
            'birthday': ugettext_lazy('Введите дату рождения'),
            'phone': ugettext_lazy('Введите номер телефона'),
            'email': ugettext_lazy('Введите E-mail'),
            'username': ugettext_lazy('Введите username'),
            'avatar': ugettext_lazy('Ваше фото-avatar'),
            'code_word': ugettext_lazy('Кодовое слово'),
            'number_btc': ugettext_lazy('Номер публичного кошелька BTC'),
            'whatsapp': ugettext_lazy('Ссылка на Ваш whatsapp'),
            'telegram': ugettext_lazy('Ссылка на Ваш telegram'),
            }


class InputPromocodForm(ModelForm):

    class Meta:
        model = Promocode
        fields = ['promo_code']
        widgets = {

            'promo_code': forms.TextInput(
                attrs={
                    'class': 'form__control',
                    'placeholder': 'Введите промокод'
                },
            )
        }


class CreatePromocodForm(forms.Form):
    quantity_promocode = forms.CharField(
        label='label', max_length=10, widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'Введите количество'}))

    def create_promocode(self):
        # send email using the self.cleaned_data dictionary
        return int(self.cleaned_data['quantity_promocode'])
        # promocodes = get_promo_code(5, int(self.cleaned_data['quantity_promocode']))
        # print('self', int(self.cleaned_data['quantity_promocode']))

# class CustomAuthForm(AuthenticationForm):
#     username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Email'}))
#     password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
