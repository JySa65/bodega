# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from bod import forms, models
from login.views import LoginRequiredMixin
# Create your views here.
class ProductosListView(LoginRequiredMixin, ListView):
	model = models.ProductoModel
	template_name = 'producto/productomodel_list.html'

class ProductosDetailView(LoginRequiredMixin, DetailView):
	model = models.ProductoModel
	template_name = 'producto/productomodel_detail.html'

class ProductosCreateView(LoginRequiredMixin, CreateView):
	model = models.ProductoModel
	second_model = models.CalculoModel
	form_class = forms.ProductoForm
	success_url = reverse_lazy('producto:list-producto')
	template_name = 'producto/productomodel_form.html'

	def get_context_data(self, **kwargs):
	    context = super(ProductosCreateView, self).get_context_data(**kwargs)
	    context["datalist"] = models.CategoriaModel.objects.all()
	    return context

	def form_valid(self, form):
                _object = form.save()
                calculo = self.second_model(producto=_object)
                calculo.save()
                return super(ProductosCreateView, self).form_valid(form)

class ProductosUpdateView(LoginRequiredMixin, UpdateView):
	model = models.ProductoModel
	form_class = forms.ProductoForm
	success_url = reverse_lazy('producto:list-producto')
	template_name = 'producto/productomodel_form.html'

class ProductosDeleteView(LoginRequiredMixin, DeleteView):
	model = models.ProductoModel
	success_url = reverse_lazy('producto:list-producto')
	template_name = 'producto/productomodel_confirm_delete.html'
