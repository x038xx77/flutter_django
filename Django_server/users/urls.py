from django.conf.urls import url
from django.urls import include, path
# from users.views import ELoginView

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    # path("auth/", ELoginView.as_view(), name='login'),
    path("auth/", include("django.contrib.auth.urls")),
    url('change/'r'(?P<user_id>\d+)/$',
        views.UpdatUserView.as_view(), name='users_edit'),
    path(
        'confirm_update_profile/',
        views.ConfirmUpdateProfileView.as_view(),
        name='confirm_update_profile'),
]
