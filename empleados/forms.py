from django import forms
from .models import Empleado

import re
from datetime import datetime
from bootstrap_datepicker_plus.widgets import DatePickerInput

def match_string(cadena, expresion_regular):
    if re.search(expresion_regular, cadena):
        return True
    else:
        return False

def fecha_es_menor(date):
    if date > datetime.now().date():
        return False
    else:
        return True

class UpdateEmpleadoForm(forms.ModelForm):
  """Form definition for UpdateEmpleado."""

  class Meta:
    """Meta definition for UpdateEmpleadoform."""

    model = Empleado
    fields = ('nombres','apellidos','cedula','email','telefono', 'fecha_nacimiento',)
    widgets = {
      'nombres': forms.TextInput({
        'class': 'form-control my-2',
        'placeholder': 'Ingresa los nombres'
      }),
      'apellidos': forms.TextInput({
        'class': 'form-control my-2',
        'placeholder': 'Ingresa los apellidos'
      }),
      'cedula': forms.TextInput({
        'class': 'form-control my-2',
        'placeholder': 'Ingresa la cédula',
        'type': 'number'
      }),
      'email': forms.EmailInput({
        'class': 'form-control my-2',
        'placeholder': 'Ingresa el email'
      }),
      'telefono': forms.TextInput({
        'class': 'form-control my-2',
        'placeholder': 'Ingresa el télefono',
        'type': 'number'
      }),
      "fecha_nacimiento": DatePickerInput(attrs={"class": "form-control", "placeholder": "DD/MM/YYYY"})
    }
    labels = {
      'telefono': 'Número de teléfono (10 dígitos - Colombia)',
      'email': 'Correo eléctronico',
      'cedula': 'Cédula',
      'fecha_nacimiento': 'Fecha de nacimiento'
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

  def clean_fecha_nacimiento(self):
      fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')

      if (fecha_es_menor(fecha_nacimiento) == False):
        self.add_error('fecha_nacimiento', 'La fecha ingresada es mayor a la fecha actual')
      return fecha_nacimiento

  def clean_telefono(self):
    telefono = self.cleaned_data.get('telefono')
    regExTel = '^\d{10}$'

    if ((match_string(telefono, regExTel)) == False):
      self.add_error('telefono', 'Debes ingresar 10 números')
  
    return telefono

  def clean_cedula(self):
    cedula = self.cleaned_data.get('cedula')
    regEx = '^[0-9]+$'

    if (match_string(cedula, regEx) == False):
      self.add_error('cedula', 'Sólamente puedes ingresar números')

    if (len(cedula) <= 5):
      self.add_error('cedula', 'La cédula debe tener más de 5 dígitos')

    if (len(cedula) > 10):
      self.add_error('cedula', 'La cédula debe tener menos de 11 dígitos')

    return cedula


class CreateEmpleadoForm(forms.ModelForm):
  """Form definition for CreateEmpleado."""

  class Meta:
    """Meta definition for CreateEmpleadoform."""

    model = Empleado
    fields = ('nombres','apellidos','cedula','email','telefono', 'fecha_nacimiento',)
    widgets = {
      'nombres': forms.TextInput({
        'class': 'form-control my-2',
        'placeholder': 'Ingresa los nombres'
      }),
      'apellidos': forms.TextInput({
        'class': 'form-control my-2',
        'placeholder': 'Ingresa los apellidos'
      }),
      'cedula': forms.TextInput({
        'class': 'form-control my-2',
        'placeholder': 'Ingresa la cédula',
        'type': 'number'
      }),
      'email': forms.EmailInput({
        'class': 'form-control my-2',
        'placeholder': 'Ingresa el email'
      }),
      'telefono': forms.TextInput({
        'class': 'form-control my-2',
        'placeholder': 'Ingresa el télefono',
        'type': 'number'
      }),
      "fecha_nacimiento": DatePickerInput(attrs={"class": "form-control", "placeholder": "DD/MM/YYYY"})
    }
    labels = {
      'telefono': 'Número de teléfono (10 dígitos - Colombia)',
      'email': 'Correo eléctronico',
      'cedula': 'Cédula',
      'fecha_nacimiento': 'Fecha de nacimiento'
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

  def clean_fecha_nacimiento(self):
      fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')

      if (fecha_es_menor(fecha_nacimiento) == False):
        self.add_error('fecha_nacimiento', 'La fecha ingresada es mayor a la fecha actual')
      return fecha_nacimiento

  def clean_telefono(self):
    telefono = self.cleaned_data.get('telefono')
    regExTel = '^\d{10}$'

    if ((match_string(telefono, regExTel)) == False):
      self.add_error('telefono', 'Debes ingresar 10 números')
  
    return telefono

  def clean_cedula(self):
    cedula = self.cleaned_data.get('cedula')
    regEx = '^[0-9]+$'

    if (match_string(cedula, regEx) == False):
      self.add_error('cedula', 'Sólamente puedes ingresar números')

    if (len(cedula) <= 5):
      self.add_error('cedula', 'La cédula debe tener más de 5 dígitos')

    if (len(cedula) > 10):
      self.add_error('cedula', 'La cédula debe tener menos de 11 dígitos')

    return cedula
