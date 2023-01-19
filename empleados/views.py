from django.shortcuts import render

from django.views.generic import (
  ListView
)

from .models import Empleado
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.


class EmpleadosListView(LoginRequiredMixin ,ListView):
    model = Empleado
    template_name = "empleados/lista-empleados.html"
    context_object_name = 'empleados'
    login_url = reverse_lazy('users:sign-in')
