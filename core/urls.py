from django.urls import path
from . import views
from django.shortcuts import render, redirect

urlpatterns = [
    path('', views.home, name='home'), # La página de inicio
    path('xss/', views.prueba_xss, name='prueba_xss'),
    path('csrf/', views.prueba_csrf, name='prueba_csrf'),
    path('clickjacking/', views.prueba_clickjacking, name='prueba_clickjacking'),
]
