from django.urls import path

app_name = 'empleados'

from .views import EmpleadosListView, EmpleadosDetailView

urlpatterns = [
  path('empleados/lista', EmpleadosListView.as_view(), name='listar-empleados'),
  path('empleados/editar/<int:pk>/', EmpleadosDetailView.as_view(), name='editar-empleados')
]