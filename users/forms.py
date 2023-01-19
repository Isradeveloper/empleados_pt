from django import forms

from .models import User

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
