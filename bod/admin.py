# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from bod.models import *
# Register your models here.

admin.site.register(EmpresaModel)
admin.site.register(CategoriaModel)
admin.site.register(DescripcionModel)
admin.site.register(FacturaModel)
admin.site.register(ProductoModel)
admin.site.register(PrecioModel)
admin.site.register(VentaModel)