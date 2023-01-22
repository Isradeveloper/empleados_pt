from django.urls import path

app_name = 'empleados'

from .views import EmpleadosListView, EmpleadosUpdateView, EmpleadosDeleteView, EmpleadosCreateView

urlpatterns = [
  path('empleados/lista', EmpleadosListView.as_view(), name='listar-empleados'),
  path('empleados/editar/<int:pk>/', EmpleadosUpdateView.as_view(), name='editar-empleado'),
  path('empleados/eliminar/<int:pk>/', EmpleadosDeleteView.as_view(), name='eliminar-empleado'),
  path('empleados/agregar/', EmpleadosCreateView.as_view(), name='agregar-empleado')
]