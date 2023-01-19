from django.shortcuts import render

from django.views.generic import (
  TemplateView
)

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

# Create your views here.

class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = "home/home-page.html"
    login_url = reverse_lazy('users:sign-in')

