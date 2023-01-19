from django.urls import path

from .views import UserRegisterView

app_name = 'users'

urlpatterns = [
  path('sign-up/', UserRegisterView.as_view(), name='sign-up')
]