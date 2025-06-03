from django.shortcuts import render
from . models import *

def service(request):
    service_data = {
        'plum_data': Plumbers.objects.all(),
        'elec_data': Electricians.objects.all()
    }
    return render(request, 'service.html', service_data)