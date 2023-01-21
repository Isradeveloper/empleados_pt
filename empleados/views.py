from django.shortcuts import render

from django.views.generic import (
  ListView, UpdateView
)

from .models import Empleado
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UpdateEmpleadoForm

# Create your views here.


class EmpleadosListView(LoginRequiredMixin ,ListView):
    model = Empleado
    template_name = "empleados/lista-empleados.html"
    context_object_name = 'empleados'
    login_url = reverse_lazy('users:sign-in')


class EmpleadosDetailView(UpdateView):
    model = Empleado
    form_class = UpdateEmpleadoForm
    template_name = "empleados/edit-empleado.html"
    context_object_name = 'empleados:editar-empleados'
    success_url = reverse_lazy('empleados:listar-empleados')



