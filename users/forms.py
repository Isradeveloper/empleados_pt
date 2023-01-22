from django import forms

from .models import User

from django.contrib.auth import authenticate

import re

def match_string(cadena, expresion_regular):
    if re.search(expresion_regular, cadena):
        return True
    else:
        return False

class UserRegisterForm(forms.ModelForm):
  """Form definition for UserRegister."""

  password = forms.CharField(
    required=True,
    label='Contraseña',
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Ingresa la contraseña'
      }
    )
  )

  passwordrepeat = forms.CharField(
    required=True,
    label='Repita la contraseña',
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Repite la contraseña'
      }
    )
  )

  class Meta:
    """Meta definition for UserRegisterform."""

    model = User
    fields = (
      'username',
      'email',
      'nombres',
      'apellidos',
      'genero',
    )

    widgets = {
    'username': forms.TextInput({
      'class': 'form-control my-2',
      'placeholder': 'Ingresa el nombre de usuario'
    }),
    'email': forms.EmailInput({
      'class': 'form-control my-2',
      'placeholder': 'Ingresa tu email'
    }),
    'nombres': forms.TextInput({
      'class': 'form-control my-2',
      'placeholder': 'Ingresa tus nombres'
    }),
    'apellidos': forms.TextInput({
      'class': 'form-control my-2',
      'placeholder': 'Ingresa tus apellidos'
    }),
    'genero': forms.Select({
      'class': 'form-control my-2',
    })
  }

  
  
  def clean_passwordrepeat(self):
    passwordrepeat = self.cleaned_data.get('passwordrepeat')
  
    # TODO Validation

    if(self.cleaned_data['password'] != self.cleaned_data['passwordrepeat']):
      self.add_error('passwordrepeat', 'Las contraseñas no coinciden')
  
    if (len(passwordrepeat) <= 5):
      self.add_error('passwordrepeat', 'La contraseña debe tener cómo mínimo 6 carácteres')
    return passwordrepeat

  def clean_password(self):
    password = self.cleaned_data.get('password')
  
    # TODO Validation
  
    if (len(password) <= 5):
      self.add_error('password', 'La contraseña debe tener cómo mínimo 6 carácteres')
    return password

  def clean_username(self):
    username = self.cleaned_data.get('username')
  
    # TODO Validation
    if (len(username) <= 2):
      self.add_error('username', 'El username debe tener como mínimo 3 carácteres')
  
    return username

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

class UserUpdateForm(forms.ModelForm):
  """Form definition for UserRegister."""

  class Meta:
    """Meta definition for UserRegisterform."""

    model = User
    fields = (
      'username',
      'email',
      'nombres',
      'apellidos',
      'genero',
    )

    widgets = {
    'username': forms.TextInput({
      'class': 'form-control my-2',
      'placeholder': 'Ingresa el nombre de usuario'
    }),
    'email': forms.EmailInput({
      'class': 'form-control my-2',
      'placeholder': 'Ingresa tu email'
    }),
    'nombres': forms.TextInput({
      'class': 'form-control my-2',
      'placeholder': 'Ingresa tus nombres'
    }),
    'apellidos': forms.TextInput({
      'class': 'form-control my-2',
      'placeholder': 'Ingresa tus apellidos'
    }),
    'genero': forms.Select({
      'class': 'form-control my-2',
    })
  }

  
  def clean_username(self):
    username = self.cleaned_data.get('username')
  
    # TODO Validation
    if (len(username) <= 2):
      self.add_error('username', 'El username debe tener como mínimo 3 carácteres')
  
    return username

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


class UserLoginForm(forms.Form):
  """UserLoginForm definition."""

  # TODO: Define form fields here
  username = forms.CharField(
    max_length=10,
    required=True,
    label='Nombre de usuario',
    widget=forms.TextInput({
      'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Ingresa nombre de usuario',
        'autocomplete': 'off'
    })
  )

  password = forms.CharField(
    required=True,
    label='Contraseña',
    widget=forms.PasswordInput({
      'class': 'form-control my-2',
        'id': 'floatingInput',
        'placeholder': 'Ingresa contraseña',
        'autocomplete': 'off'
    })
  )

  def clean(self):
    cleaned_data = super(UserLoginForm, self).clean()

    username = self.cleaned_data['username']
    password = self.cleaned_data['password']

    if (not authenticate(username = username, password = password)):
      raise forms.ValidationError('Los datos del usuario no son correctos')

    return self.cleaned_data

  def clean_password(self):
    password = self.cleaned_data.get('password')
    
    # TODO Validation
    if (len(password) <= 5):
      self.add_error('password', 'La contraseña debe tener como mínimo 6 carácteres')
    return password

  def clean_username(self):
    username = self.cleaned_data.get('username')
  
    # TODO Validation
    if (len(username) <= 2):
      self.add_error('username', 'El username debe tener como mínimo 3 carácteres')
  
    return username

class UpdatePasswordForm(forms.Form):

  def __init__(self, *args, **kwargs):
    self.request = kwargs.pop('request', None)
    super().__init__(*args, **kwargs)

  """UpdatePasswordForm definition."""

  # TODO: Define form fields here

  oldpassword = forms.CharField(
    required=True,
    label='Contraseña actual',
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control my-2',
        'placeholder': 'Contraseña actual'
      }
    )
  )

  password = forms.CharField(
    required=True,
    label='Contraseña nueva',
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control my-2',
        'placeholder': 'Contraseña nueva'
      }
    )
  )

  passwordrepeat = forms.CharField(
    required=True,
    label='Repita la contraseña',
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control my-2',
        'placeholder': 'Repita contraseña nueva'
      }
    )
  )

  def clean_oldpassword(self):
    oldpassword = self.cleaned_data.get('oldpassword')
    usuario = self.request.user
  
    # TODO Validation

    if (len(oldpassword) <= 5):
      self.add_error('oldpassword', 'La contraseña debe tener como mínimo 6 carácteres')

    if (not authenticate(username=usuario.username, password=oldpassword)):
      self.add_error('oldpassword', 'Esta contraseña es incorrecta')

    return oldpassword

  def clean_password(self):
    password = self.cleaned_data.get('password')

    # TODO Validation

    if (len(password) <= 5):
      self.add_error('password', 'La contraseña debe tener como mínimo 6 carácteres')

    return password

  def clean_passwordrepeat(self):
    passwordrepeat = self.cleaned_data.get('passwordrepeat')
    password = self.cleaned_data.get('password')
      
    # TODO Validation

    if (len(passwordrepeat) <= 5):
      self.add_error('passwordrepeat', 'La contraseña debe tener como mínimo 6 carácteres')

    if (password != passwordrepeat):
      self.add_error('passwordrepeat', 'Las contraseñas no coinciden')

    return passwordrepeat



