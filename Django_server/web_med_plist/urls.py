"""web_med_plist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView
from django.contrib.flatpages import views
import debug_toolbar
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    url(
        r'^favicon\.ico$',
        RedirectView.as_view(
            url='/static/images/favicon.ico'), name='favicon'),
    path('admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    path('', include('users.urls')),
    path('api/', include('api.urls')),
    path('', include('chat.urls')),
    path('', include('src.videoch_chat.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('main_app.urls')),
    path('', include('sendemail.urls')),
    path(
        'info/',
        views.flatpage, {'url': '/info/'}, name='info'),
    path(
        'why/',
        views.flatpage, {'url': '/why/'}, name='why'),
)

if settings.DEBUG:

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
