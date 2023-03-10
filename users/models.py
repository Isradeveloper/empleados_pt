from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.

GENDER_CHOICES = (
  ('M', 'Másculino'),
  ('F', 'Femenino'),
  ('O', 'Otros'),
)

class User(AbstractBaseUser, PermissionsMixin): 
  username = models.CharField(max_length=10, unique=True, blank=False)
  email = models.EmailField(max_length=254, blank=False, unique=True)
  nombres = models.CharField(max_length=50, blank=True)
  apellidos = models.CharField(max_length=50, blank=True)
  genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)
  cod_registro = models.CharField(max_length=6, blank=True)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)

  USERNAME_FIELD = 'username'

  REQUIRED_FIELDS = ['email']

  objects = UserManager()

  def get_shortname(self):
    return self.username

  def get_full_name(self):
    return (f'{self.nombres} {self.apellidos}')