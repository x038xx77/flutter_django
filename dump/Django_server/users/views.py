

from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from . forms import CreationForm, UpdateUserForm
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.views.generic.base import TemplateView

# from cilia_assistant.models import Ip_Cilia_Assistant, Cilia_Assistant
from django.utils import timezone

User = get_user_model()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("index")
    template_name = 'signup.html'

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class UpdatUserView(LoginRequiredMixin, UpdateView):
    """Редактирование данных пользователя."""
    model = User
    form_class = UpdateUserForm

    template_name = 'signup.html'
    pk_url_kwarg = 'user_id'
    success_url = reverse_lazy('index')


class ConfirmUpdateProfileView(TemplateView):
    template_name = 'change_confirm_profile_user.html'



# class ELoginView(View):

#     def get(self, request):
#         # если пользователь авторизован, то делаем редирект на главную страницу
#         if auth.get_user(request).is_authenticated:
#             return redirect('/')
#         else:
#             return render(
#                 request,
#                 'registration/login.html')

#     # https://evileg.com/ru/post/214/
#     # https://evileg.com/ru/post/283/#comment-2200
#     def post(self, request, *args, **kwargs):
#         form = AuthenticationForm(request, data=request.POST)
#         ip = get_client_ip(request)
#         # получаем или создаём новую запись об IP, с которого вводится пароль, на предмет блокировки # noqa
#         obj_trafik, created = Cilia_Assistant.objects.get_or_create(
#                 title='Cтраница регистрации', slug='create_user_cilia')
#         create_user_cilia = get_object_or_404(
#                 Cilia_Assistant, slug='create_user_cilia')
#         obj, created = Ip_Cilia_Assistant.objects.get_or_create(
#             defaults={
#                 'ip_address': ip,
#                 'time_unblock': timezone.now()
#                 },
#             ip_address=ip,
#             traffic_cilia = create_user_cilia
#             )

#         # если IP заблокирован и время разблокировки не настало
#         if obj.status is True and obj.time_unblock > timezone.now():
#             if obj.attempts == 3 or obj.attempts == 6:
#                 # то открываем страницу с сообщением о блокировки на 15 минут при 3 и 6 неудачных попытках входа # noqa
#                 return render(
#                     request,
#                     'block_15_minutes.html', {"foo": "bar"})

#             elif obj.attempts == 9:
#                 # или открываем страницу о блокировке на 24 часа, при 9 неудачных попытках входа # noqa
#                 return render(
#                     request,
#                     'block_24_hours.html')
#         elif obj.status is True and obj.time_unblock < timezone.now():
#             # если IP заблокирован, но время разблокировки настало, то разблокируем IP # noqa
#             obj.status = False
#             obj.save()

#         if form.is_valid():
#             auth.login(request, form.get_user())
#             obj.delete()
#             return HttpResponseRedirect(reverse_lazy('index'))

#         else:
#             obj.attempts = obj.attempts + 1
#             if obj.attempts == 3 or obj.attempts == 6:
#                 obj.time_unblock = timezone.now() + timezone.timedelta(
#                     minutes=15)
#                 obj.status = True
#             elif obj.attempts == 9:
#                 obj.time_unblock = timezone.now() + timezone.timedelta(1)
#                 obj.status = True
#             elif obj.attempts > 9:
#                 obj.attempts = 1
#             obj.save()
#         return render(
#                 request,
#                 'registration/login.html')
