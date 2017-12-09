from django.conf.urls import url
from bod.views import *

urlpatterns = [
    url(r'^list/$', EmpresasListView.as_view(), name='list-empresa'),
    url(r'^create/$', EmpresasCreateView.as_view(), name='create-empresa'),
    url(r'^detail/(?P<pk>[-\ \w]+)/$', EmpresasDetailView.as_view(), name='detail-empresa'),
    url(r'^update/(?P<pk>[-\ \w]+)/$', EmpresasUpdateView.as_view(), name='update-empresa'),
    url(r'^delete/(?P<pk>[-\ \w]+)/$', EmpresasDeleteView.as_view(), name='delete-empresa'),
]


