from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.service, name='service'),
    path('elec_serv_booking/<int:pk>', views.electric_service_booking, name='electric_service_booking'),
    path('electrical_service_booking/', views.electrical_service_booking, name='electrical_service_booking'),
    path('success_booking/', views.success_booking, name='success_booking'),
]
