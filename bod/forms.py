from django import forms
from bod.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = EmpresaModel
        fields = ('tipo_rif',
                  'rif',
				  'nombre',
				  'direccion',)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaModel
        fields = ('departamento',)

class FacturaForm(forms.ModelForm):
    empresa = forms.CharField(max_length=100,)
    class Meta:
        model = FacturaModel
        fields = ('codigo',
                  'fecha',
				  'empresa',)
        widgets = {
            'fecha': DateInput(format = '%Y-%m-%d'),

        }
    
class ProductoForm(forms.ModelForm):
    class Meta:
        model = ProductoModel
        fields = ('codigo',
				  'producto',
				  'categoria',)
    
class PrecioForm(forms.ModelForm):
    class Meta:
        model = PrecioModel
        fields = ('precio_compra',
				  'precio_venta',
				  'producto',)
    
class DescripcionForm(forms.ModelForm):
    class Meta:
        model = DescripcionModel
        fields = ('cantidad',
				  'exento',
				  'producto',
				  'codfac',)
    
class VentaForm(forms.ModelForm):
    class Meta:
        model = VentaModel
        fields = ('cantidad',
				  'producto',)
    