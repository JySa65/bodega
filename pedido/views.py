# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from bod import forms, models
from login.views import LoginRequiredMixin
# Create your views here.

class PedidoCreateView(CreateView):
	model = models.FacturaModel
	second_model = models.EmpresaModel
	form_class = forms.FacturaForm
	second_form_class = forms.EmpresaModel
	template_name = 'pedido/pedido_form.html'


	def post(self, *args, **kwargs):
		message = ""
		form = self.form_class(self.request.POST)
		empresa = self.second_model.objects.get(pk=self.request.POST.get("empresa"))
		cod = self.model.objects.filter(codigo=str(self.request.POST.get("codigo"))).first()
		if not cod:
			sav = self.model.objects.create(codigo=self.request.POST.get("codigo"), fecha=self.request.POST.get("fecha"), empresa=empresa)
			message = "Creado Exitosamente"
		else:
			message = "Este Codigo Ya Existe"
			return render(self.request, self.template_name, {'form["codigo"]':2323})
		return HttpResponse(message)


class BuscadorEmpresaView(TemplateView):
	model = models.EmpresaModel

	def get(self, *args, **kwargs):
		palabra = self.request.GET.get("name")
		empresa = self.model.objects.filter(nombre__contains = str(palabra))
		data = {}
		acum = 0
		for i in empresa:
			data[acum]={"pk": i.pk, "nombre": i.nombre, "rif": i.rif}
			acum+=1
		return JsonResponse(data)

class BuscadorProductoView(TemplateView):
	model = models.ProductoModel

	def get(self, *args, **kwargs):
		palabra = self.request.GET.get("name")
		empresa = self.model.objects.filter(producto__contains = str(palabra))
		data = {}
		acum = 0
		for i in empresa:
                        #upc: ultimo precio compra - venta
			data[acum]={"pk": i.pk, "codigo": i.codigo, "nombre": i.producto, "upc": "", "upv": "", "exento": ""}
			acum+=1
		return JsonResponse(data)

