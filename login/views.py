# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, FormView, View
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from django.views.defaults import page_not_found

# Create your views here.
class LoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('login:panel-login'))
        else:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class LoginRequiredMixin2(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('login:index'))
        else:
            return super(LoginRequiredMixin2, self).dispatch(request, *args, **kwargs)

class Error404(TemplateView):
    template_name = '404.html'

class Error500(TemplateView):
    template_name = '500.html'


class LoginView(LoginRequiredMixin2, FormView):
    form_class = AuthenticationForm
    template_name = "login/login.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form, 'message': ''})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy("login:index"))
            else:
                return HttpResponse('no esta activo')
        else:
            mensaje = "Usuario o Contraseña Incorrecta"
            return render(request, self.template_name, {'form': self.form_class, 'message': mensaje})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy("login:panel-login"))


from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

class ChangePassword(LoginRequiredMixin, FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("login:panel-login")
    template_name = 'login/change_password.html'

    def get_form_kwargs(self):
        kwargs = super(ChangePassword, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        logout(self.request)
        return super(ChangePassword, self).form_valid(form)
