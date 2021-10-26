from django.urls import path
from django.conf.urls import url
from django.views.defaults import server_error, page_not_found, permission_denied

from . import views


urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('projects/', views.ProjectsPage.as_view(), name='projects'),
]