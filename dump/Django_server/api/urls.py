from django.urls import path
from .views import UserRecordView
from rest_framework.authtoken import views


urlpatterns = [
    path('v1/user/', UserRecordView.as_view(), name='users'),
    path('v1/api-token-auth/', views.obtain_auth_token, name='api-token-auth'),

]

handler400 = 'rest_framework.exceptions.bad_request'
