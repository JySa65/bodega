# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from bod import forms, models
from login.views import LoginRequiredMixin
# Create your views here.

class PedidoCreateView(CreateView):
	model = models.FacturaModel
	form_class = forms.FacturaForm
	template_name = 'pedido/pedido_form.html'

class BuscadorEmpresaView(TemplateView):
	model = models.EmpresaModel
	
	def get(self, *args, **kwargs):
		palabra = self.request.GET.get("name")
		empresa = self.model.objects.filter(nombre__contains = str(palabra))
		data = {}
		acum = 0
		for i in empresa:
			data[acum] = [{"pk": i.pk, "nombre": i.nombre, "rif": i.rif}]
			acum+=1
		return JsonResponse(data)


