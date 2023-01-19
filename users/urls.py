from django.urls import path

from .views import UserRegisterView, UserLoginView, UserLogout, UpdatePasswordView, VerificationView

app_name = 'users'

urlpatterns = [
  path('sign-up/', UserRegisterView.as_view(), name='sign-up'),
  path('sign-in/', UserLoginView.as_view(), name='sign-in'),
  path('logout/', UserLogout.as_view(), name='logout'),
  path('update-password', UpdatePasswordView.as_view(), name='update-password'),
  path('user-verification', VerificationView.as_view(), name='verification'),
]