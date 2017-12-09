from django.conf.urls import url
from pedido.views import *

urlpatterns = [
    url(r'^create/$', PedidoCreateView.as_view(), name='create-pedido'),
    url(r'^buscar/empresa/$', BuscadorEmpresaView.as_view(), name='buscar-empresa'),
    
]


