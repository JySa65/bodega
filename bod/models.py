# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class EmpresaModel(models.Model):
	tipo = (
			('J','J'),
			('V','V'),
			('E','E'),
			('P','P'),
			('G','G'),
		)
	tipo_rif = models.CharField(max_length=10, null=False, blank=False, choices=tipo)
	rif = models.CharField(max_length=10, null=False, blank=False, unique=True)
	nombre = models.CharField(max_length=100, null=False, blank=False)
	direccion = models.TextField()

	def __str__(self):
		return str(self.nombre)
    
class CategoriaModel(models.Model):
	departamento = models.CharField(max_length=10, null=False, blank=False)

	def __str__(self):
		return str(self.departamento)

class FacturaModel(models.Model):
	codigo = models.CharField(max_length=10, null=False, blank=False, unique=True)
	fecha = models.DateField()
	empresa = models.ForeignKey(
        EmpresaModel,
        on_delete=models.CASCADE,
    )
	def __str__(self):
		return str(self.codigo)

class ProductoModel(models.Model):
	codigo = models.CharField(max_length=50, null=False, blank=False)
	producto = models.CharField(max_length=100, null=False, blank=False)
	categoria = models.ForeignKey(
		CategoriaModel, null=False, blank=False,
		on_delete=models.CASCADE,
		)
	
	def __str__(self):
		return str(self.producto)

class PrecioModel(models.Model):
	fecha = models.DateField(auto_now_add=True,)
	precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
	precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
	producto = models.ForeignKey(
		ProductoModel,
		on_delete=models.CASCADE)

	def __str__(self):
		return str(self.precio)

class DescripcionModel(models.Model):
	cantidad = models.IntegerField(default=0, null=False, blank=False)
	exento = models.BooleanField(default=False)
	producto = models.ForeignKey(
		ProductoModel, 
		on_delete=models.CASCADE)
	codfac = models.ForeignKey(
		FacturaModel,
		on_delete=models.CASCADE,
		)

	def __str__(self):
		return str(self.nombre) 

class VentaModel(models.Model):
	cantidad = models.DecimalField(max_digits=10, decimal_places=2)
	producto = models.ForeignKey(
		ProductoModel,
		on_delete=models.CASCADE)
	def __str__(self):
		return str(self.cantidad)
    

class CalculoModel(models.Model):
        producto = models.ForeignKey(
		ProductoModel,
		on_delete=models.CASCADE)
        n_compra = models.IntegerField(default=0)
        n_venta = models.IntegerField(default=0)

        def __str__(self):
                return str(self.producto)
        
