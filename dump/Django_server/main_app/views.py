from django.contrib import messages
from django.db.models import Sum
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView, View
from django.views.generic import (
    ListView,
    DetailView, CreateView,
    UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from requests.api import request
import urllib
from django.core.signing import Signer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class IndexPage(TemplateView):
    template_name = 'index.html'

class ProjectsPage(ListView):
    """ список квестов """
    template_name = 'project/projects_page.html'

    def get_queryset(self):
        
        queryset = User.objects.all()
        return queryset

class InfoMenuPages(ListView):
    template_name = 'info_site/info_page_site.html'