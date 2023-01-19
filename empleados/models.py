from django.db import models

# Create your models here.

class Empleado(models.Model):
  """Model definition for Empleado."""

  # TODO: Define fields here
  nombres = models.CharField(max_length=50, blank=False)
  apellidos = models.CharField(max_length=50, blank=False)
  cedula = models.IntegerField(blank=False)
  email = models.EmailField(max_length=254, blank=False)
  fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False, blank=False)
  telefono = models.IntegerField(blank=False)

  class Meta:
    """Meta definition for Empleado."""

    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'

  def __str__(self):
    """Unicode representation of Empleado."""
    return(f'[{self.id}] {self.nombres} {self.apellidos} {self.cedula}')

  def get_full_name(self):
    return (f'{self.nombres} {self.apellidos}')
