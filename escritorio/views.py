from django.contrib.auth.decorators import login_required
from django.shortcuts import render 
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView
from escritorio.models import Relatorio
from django.urls import reverse
from django.views.generic.edit import FormView
from .forms import FileFieldForm
from django.core import serializers
from django.http import JsonResponse
from django.views import View
import pandas as pd


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = "escritorio/home.html"


@method_decorator(login_required, name='dispatch')
class RelatorioListView(ListView):
    template_name = "escritorio/arquivos.html"
    model = Relatorio
    context_object_name = 'arquivos'   
    queryset = Relatorio.objects.all() 


@method_decorator(login_required, name='dispatch')
class RelatorioCreateView(FormView):
    template_name = "escritorio/create_relatorio.html"
    model = Relatorio
    fields = ['nome', 'arquivo']
    form_class = FileFieldForm

    def get_success_url(self):
        return reverse('escritorio:lista-arquivos')
    
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class RelatorioDetailView(DetailView):

    template_name = "escritorio/arquivo_detail.html"
    model = Relatorio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context