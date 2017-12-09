from django.conf.urls import url
from producto.views import *

urlpatterns = [
    url(r'^list/', ProductosListView.as_view(), name='list-producto'),
    url(r'^create/$', ProductosCreateView.as_view(), name='create-producto'),
    url(r'^detail/(?P<pk>[-\ \w]+)/$', ProductosDetailView.as_view(), name='detail-producto'),
    url(r'^update/(?P<pk>[-\ \w]+)/$', ProductosUpdateView.as_view(), name='update-producto'),
    url(r'^delete/(?P<pk>[-\ \w]+)/$', ProductosDeleteView.as_view(), name='delete-producto'),
]

