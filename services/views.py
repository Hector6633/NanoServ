from django.shortcuts import render
from . models import *

def service(request):
    service_data = {
        'plum_data': Plumbers.objects.all(),
        'elec_data': Electricians.objects.all(),
        'tv_data': SmartTv.objects.all(),
    }
    return render(request, 'service.html', service_data)

def electric_service_booking(request, pk):
    electric_service_data = {
        'electric_data' : Electricians.objects.get(pk=pk),
    }
    return render(request, 'service_booking.html', electric_service_data)