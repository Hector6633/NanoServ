from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.electricians, name='service'),
    path('service/', views.plumbers, name='service'),
]
