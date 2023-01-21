from django import forms
from .models import Empleado

class UpdateEmpleadoForm(forms.ModelForm):
  """Form definition for UpdateEmpleado."""

  class Meta:
    """Meta definition for UpdateEmpleadoform."""

    model = Empleado
    fields = ('nombres','apellidos','cedula','email','telefono', 'fecha_nacimiento',)
    widgets = {
      'nombres': forms.TextInput({
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'Ingresa los nombres'
      }),
      'apellidos': forms.TextInput({
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'Ingresa los apellidos'
      }),
      'cedula': forms.NumberInput({
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'Ingresa la cédula',
        'maxlength': '3'
      }),
      'email': forms.EmailInput({
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'Ingresa el email'
      }),
      'telefono': forms.NumberInput({
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': 'Ingresa el télefono'
      }),
      'fecha_nacimiento': forms.DateInput({
        'class': 'form-control',
        'id': 'floatingInput',
        'placeholder': '(dd/MM/YYYY)'
      })
    }

  def clean_nombres(self):
    nombres = self.cleaned_data.get('nombres')

    if (len(nombres) < 3):
      self.add_error('nombres', 'El nombre debe tener más de 2 carácteres')
  
    return nombres

