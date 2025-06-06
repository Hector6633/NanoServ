from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.service, name='service'),
    path('service_booking/<int:pk>', views.electric_service_booking, name='electric_service_booking'),
]
