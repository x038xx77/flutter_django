from django.contrib import admin
from django.urls import path

from .views import contactView, successView

urlpatterns = [
    path('contact_email/', contactView, name='contact_email'),
    path('success_email/', successView, name='success_email'),
]
