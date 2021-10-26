from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Promocode

User = get_user_model()


@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    list_display = (
        'promo_code', 'author', 'is_issued_promo_code', 'is_used_promo_code')
    search_fields = ('promo_code',)
    list_filter = ('is_issued_promo_code',)
    empty_value_display = '---'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'username', 'role',
        'location', 'phone',
        'birthday', 'avatar', 'first_name', 'last_name')
    empty_value_display = '---'
