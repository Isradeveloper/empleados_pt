from django.shortcuts import render

from .models import User

from django.views.generic import (
  CreateView
)
from django.views.generic.edit import FormView 

from .forms import UserRegisterForm

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
