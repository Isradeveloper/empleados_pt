from django.urls import path

app_name = 'empleados'

from .views import EmpleadosListView

urlpatterns = [
  path('empleados/lista', EmpleadosListView.as_view(), name='listar-empleados')
]