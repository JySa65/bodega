# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from bod import forms, models
from login.views import LoginRequiredMixin
# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
	template_name = 'bod/index.html'

class EmpresasListView(LoginRequiredMixin, ListView):
	model = models.EmpresaModel

class EmpresasDetailView(LoginRequiredMixin, DetailView):
	model = models.EmpresaModel

class EmpresasCreateView(LoginRequiredMixin, CreateView):
	model = models.EmpresaModel
	form_class = forms.EmpresaForm
	success_url = reverse_lazy('bodega:list-empresa')

class EmpresasUpdateView(LoginRequiredMixin, UpdateView):
	model = models.EmpresaModel
	form_class = forms.EmpresaForm
	success_url = reverse_lazy('bodega:list-empresa')

class EmpresasDeleteView(LoginRequiredMixin, DeleteView):
	model = models.EmpresaModel
	success_url = reverse_lazy('bodega:list-empresa')