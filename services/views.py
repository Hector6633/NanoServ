from django.shortcuts import render
from . models import *
# Create your views here.
def electricians(request):
    elec_data = {
        'elec_data': Electricians.objects.all()
    }
    return render(request, 'service.html', elec_data)

def plumbers(request):
    plum_data = {
        'plum_data': Plumbers.objects.all()
    }
    return render(request, 'service.html', plum_data)