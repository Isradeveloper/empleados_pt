from django.shortcuts import render

from .models import User

from django.urls import reverse_lazy, reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect

from django.views.generic import (
  CreateView,
  View
)

from django.views.generic.edit import FormView 

from .forms import UserRegisterForm, UserLoginForm, UpdatePasswordForm

# Create your views here.

class UserRegisterView(FormView):
  template_name = 'users/signup.html'
  form_class = UserRegisterForm
  success_url = '/'

  def form_valid(self, form):

    User.objects.create_user(
      form.cleaned_data['username'],
      form.cleaned_data['email'],
      form.cleaned_data['password'],
      # form.cleaned_data['passwordrepeat'],
      nombres = form.cleaned_data['nombres'],
      apellidos = form.cleaned_data['apellidos'],
      genero = form.cleaned_data['genero'],
    )

    return super().form_valid(form)

class UserLoginView(FormView):
  template_name = 'users/signin.html'
  form_class = UserLoginForm
  success_url = reverse_lazy('home:panel')

  def form_valid(self, form):

    user = authenticate(
      username = form.cleaned_data['username'],
      password = form.cleaned_data['password']
    )

    login(self.request, user)

    return super().form_valid(form)

class UserLogout(View):
  def get(self, request, *args, **kargs):
    logout(request)
    return HttpResponseRedirect(
      reverse('users:sign-in')
    )

class UpdatePasswordView(LoginRequiredMixin,FormView):
  template_name = 'users/update-password.html'
  form_class = UpdatePasswordForm
  success_url = reverse_lazy('users:sign-in')
  login_url = reverse_lazy('users:sign-in')

  def form_valid(self, form):
    usuario = self.request.user
    user = authenticate(
      username = usuario.username,
      password = form.cleaned_data['oldpassword']
    )

    if user:
      new_password = form.cleaned_data['password']
      usuario.set_password(new_password)
      usuario.save()
      logout(self.request)

    return super().form_valid(form)