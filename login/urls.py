from django.conf.urls import url
from login.views import *
from bod.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
	url(r'^login/$', LoginView.as_view(), name='panel-login'),
	url(r'^logout/$', LogoutView.as_view(), name='panel-logout'),
	url(r'^change/password/$', ChangePassword.as_view(), name='change_password'),
]

