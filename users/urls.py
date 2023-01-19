from django.urls import path

from .views import UserRegisterView, UserLoginView

app_name = 'users'

urlpatterns = [
  path('sign-up/', UserRegisterView.as_view(), name='sign-up'),
  path('sign-in/', UserLoginView.as_view(), name='sign-in')
]