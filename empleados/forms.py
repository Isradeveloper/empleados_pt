from django import forms
from .models import Empleado

import re

def match_string(cadena, expresion_regular):
    if re.search(expresion_regular, cadena):
        return True
    else:
        return False

class UpdateEmpleadoForm(forms.ModelForm):
  """Form definition for UpdateEmpleado."""

  class Meta:
    """Meta definition for UpdateEmpleadoform."""

    model = Empleado
    fields = ('nombres','apellidos','cedula','email','telefono', 'fecha_nacimiento',)
    widgets = {
      'nombres': forms.TextInput({
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Ingresa los nombres'
      }),
      'apellidos': forms.TextInput({
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Ingresa los apellidos'
      }),
      'cedula': forms.NumberInput({
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Ingresa la cédula',
        'maxlength': '3'
      }),
      'email': forms.EmailInput({
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Ingresa el email'
      }),
      'telefono': forms.NumberInput({
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Ingresa el télefono'
      }),
      'fecha_nacimiento': forms.DateInput({
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': '(dd/MM/YYYY)'
      })
    }

  def clean_nombres(self):
    nombres = self.cleaned_data.get('nombres')
    expresion_regular =  "^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$"

    if (len(nombres) < 3):
      self.add_error('nombres', 'El nombre debe tener más de 2 carácteres')

    if (match_string(nombres, expresion_regular)) == False:
      self.add_error('nombres', 'El nombre sólo debe contener letras')
  
    return nombres

  def clean_apellidos(self):
    apellidos = self.cleaned_data.get('apellidos')
    expresion_regular =  "^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$"

    if (len(apellidos) < 3):
      self.add_error('apellidos', 'El apellido debe tener más de 2 carácteres')

    if (match_string(apellidos, expresion_regular)) == False:
      self.add_error('apellidos', 'El apellido sólo debe contener letras')
  
    return apellidos

class CreateEmpleadoForm(forms.ModelForm):
  """Form definition for UpdateEmpleado."""

  class Meta:
    """Meta definition for UpdateEmpleadoform."""

    model = Empleado
    fields = ('nombres','apellidos','cedula','email','telefono', 'fecha_nacimiento',)
    widgets = {
      'nombres': forms.TextInput({
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Ingresa los nombres'
      }),
      'apellidos': forms.TextInput({
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Ingresa los apellidos'
      }),
      'cedula': forms.NumberInput({
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Ingresa la cédula',
        'maxlength': '3'
      }),
      'email': forms.EmailInput({
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Ingresa el email'
      }),
      'telefono': forms.NumberInput({
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Ingresa el télefono'
      }),
      'fecha_nacimiento': forms.DateInput({
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': '(dd/MM/YYYY)'
      })
    }

  def clean_nombres(self):
    nombres = self.cleaned_data.get('nombres')
    expresion_regular =  "^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$"

    if (len(nombres) < 3):
      self.add_error('nombres', 'El nombre debe tener más de 2 carácteres')

    if (match_string(nombres, expresion_regular)) == False:
      self.add_error('nombres', 'El nombre sólo debe contener letras')
  
    return nombres

  def clean_apellidos(self):
    apellidos = self.cleaned_data.get('apellidos')
    expresion_regular =  "^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$"

    if (len(apellidos) < 3):
      self.add_error('apellidos', 'El apellido debe tener más de 2 carácteres')

    if (match_string(apellidos, expresion_regular)) == False:
      self.add_error('apellidos', 'El apellido sólo debe contener letras')
  
    return apellidos


