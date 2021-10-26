from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField


class Promocode(models.Model):
    promo_code = models.CharField(
        verbose_name='Промокод', max_length=30, blank=True)
    author = models.ForeignKey(
        'User',
        related_name='promocodes',
        on_delete=models.CASCADE,
        verbose_name='Автор промокода',
    )
    is_issued_promo_code = models.BooleanField(
        verbose_name='Промокод свободный', default=False)
    is_used_promo_code = models.BooleanField(
        verbose_name='Промокод использован', default=False)

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'

    def __str__(self):
        return self.promo_code


class User(AbstractUser):
    class UserRole(models.TextChoices):
        USER = 'user', 'user'
        MODERATOR = 'moderator', 'moderator'
        ADMIN = 'admin', 'admin'

    class Meta:
        db_table = 'auth_user'
        ordering = ('-date_joined',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    bio = models.TextField(
        max_length=500, null=True, blank=True, verbose_name='О себе')
    role = models.CharField(
        max_length=10,
        choices=UserRole.choices,
        default=UserRole.USER,
        verbose_name='Роль',
    )
    email = models.EmailField(
        unique=True, verbose_name='Почта')
    whatsapp = models.CharField(
        'Ссылка на whatsapp', max_length=50, blank=True)
    telegram = models.CharField(
        'Ссылка на telegram', max_length=50, blank=True)
    username = models.SlugField(
        max_length=20,
        unique=True,
        verbose_name='Имя пользователя',
    )
    location = models.CharField(max_length=30, blank=True, null=True)
    phone = PhoneNumberField()
    birthday = models.DateField(blank=True, null=True)
    avatar = models.ImageField(
        upload_to='users/avatar/',
        blank=True, null=True)
    promocode = models.ForeignKey(
        Promocode,
        on_delete=models.CASCADE,
        related_name='promocod',
        verbose_name='Промокод', null=True, blank=True)
    code_word = models.CharField('Кодовое слово', max_length=30)
    number_btc = models.CharField('Номер публичного кошелька BTC', max_length=100)

    objects = UserManager()

    def __str__(self):
        return self.username or self.email

    @property
    def is_admin(self):
        return self.role == self.UserRole.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.UserRole.MODERATOR
