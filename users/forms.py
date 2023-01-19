from django import forms

from .models import User

from django.http import request

from django.contrib.auth import authenticate

class UserRegisterForm(forms.ModelForm):
  """Form definition for UserRegister."""

  password = forms.CharField(
    required=True,
    label='Contraseña',
    widget=forms.PasswordInput(
      attrs={
        'placeholder': 'Contraseña'
      }
    )
  )

  passwordrepeat = forms.CharField(
    required=True,
    label='Repita la contraseña',
    widget=forms.PasswordInput(
      attrs={
        'placeholder': 'Repetir contraseña'
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

class UserLoginForm(forms.Form):
  """UserLoginForm definition."""

  # TODO: Define form fields here
  username = forms.CharField(
    max_length=10,
    required=True,
    label='Nombre de usuario',
    widget=forms.TextInput({
      'placeholder': 'username'
    })
  )

  password = forms.CharField(
    required=True,
    label='Contraseña',
    widget=forms.PasswordInput({
      'placeholder': 'password'
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
  """UpdatePasswordForm definition."""

  # TODO: Define form fields here

  oldpassword = forms.CharField(
    required=True,
    label='Contraseña actual',
    widget=forms.PasswordInput(
      attrs={
        'placeholder': 'Contraseña actual'
      }
    )
  )

  password = forms.CharField(
    required=True,
    label='Contraseña nueva',
    widget=forms.PasswordInput(
      attrs={
        'placeholder': 'Contraseña nueva'
      }
    )
  )

  passwordrepeat = forms.CharField(
    required=True,
    label='Repita la contraseña',
    widget=forms.PasswordInput(
      attrs={
        'placeholder': 'Repita contraseña nueva'
      }
    )
  )

  def clean_oldpassword(self):
    oldpassword = self.cleaned_data.get('oldpassword')
    # usuario = request.user
  
    # TODO Validation

    if (len(oldpassword) <= 5):
      self.add_error('oldpassword', 'La contraseña debe tener como mínimo 6 carácteres')

    # if (not authenticate(username=usuario.username, password=oldpassword)):
    #   self.add_error('oldpassword', 'Esta contraseña es incorrecta')

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

  
  


