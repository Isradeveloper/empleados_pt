from django.shortcuts import render

from django.core.mail import send_mail

from .models import User

from django.urls import reverse_lazy, reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect

from django.views.generic import (
  CreateView,
  View,
  UpdateView
)

from django.views.generic.edit import FormView

from .forms import UserRegisterForm, UserLoginForm, UpdatePasswordForm, UserUpdateForm

from .functions import code_generator

# Create your views here.

class UserRegisterView(FormView):
  template_name = 'users/signup.html'
  form_class = UserRegisterForm
  success_url = '/'

  def form_valid(self, form):

    codigo = code_generator()

    User.objects.create_user(
      form.cleaned_data['username'],
      form.cleaned_data['email'],
      form.cleaned_data['password'],
      # form.cleaned_data['passwordrepeat'],
      nombres = form.cleaned_data['nombres'],
      apellidos = form.cleaned_data['apellidos'],
      genero = form.cleaned_data['genero'],
      cod_registro = codigo
    )

    # # Correo
    # asunto = 'Confirmación de cuenta'
    # mensaje = f'Código de verificación {codigo}'
    # email_remitente = 'pruebasisratrujillo@gmail.com'
    # # 
    # send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email'],])

    # return HttpResponseRedirect(
    #   reverse(
    #     'users:verification'
    #   )
    # )

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
  template_name = 'users/change-password.html'
  form_class = UpdatePasswordForm
  success_url = reverse_lazy('users:sign-in')
  login_url = reverse_lazy('users:sign-in')

  def get_form_kwargs(self):
    kwargs = super().get_form_kwargs()
    kwargs['request'] = self.request
    return kwargs

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

class UserUpdateView(LoginRequiredMixin ,UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/edit-user.html"
    success_url = reverse_lazy('home:panel')
    login_url = reverse_lazy('users:sign-in')
    
    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['user'] = self.get_object()
        context['form'] = self.get_form()
        return context