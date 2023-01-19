from django.urls import path

from .views import HomePageView

app_name = 'home'

urlpatterns = [
  path('panel/', HomePageView.as_view(), name='panel')
]