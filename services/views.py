from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def service(request):
    service_data = {
        "plum_data": Plumbers.objects.all(),
        "elec_data": Electricians.objects.all(),
        "tv_data": SmartTv.objects.all(),
    }
    return render(request, "service.html", service_data)

def success_booking(request):
    return render(request, 'success_booking.html')


def electric_service_booking(request, pk):
    electric_service_data = {
        "electric_data": Electricians.objects.get(pk=pk),
    }
    return render(request, "elec_serv_booking.html", electric_service_data)


def electrical_service_booking(request):
    if request.method == "POST":
        try:
            booking_name = request.POST.get("name")
            booking_email = request.POST.get("email")
            booking_phone = request.POST.get("phone")
            booking_location = request.POST.get("location")
            booking_service = request.POST.get("service")
            booking_price = request.POST.get("price")
            booking_address = request.POST.get("address")
            booking_data = Electrical_service_booking.objects.create(
                booking_name=booking_name,
                booking_email=booking_email,
                booking_phone=booking_phone,
                booking_location=booking_location,
                booking_service=booking_service,
                booking_price=booking_price,
                booking_address=booking_address,
            )
            booking_data.save()
            success_msg = "Successfully Booked"
            messages.success(request, success_msg)
            return redirect('success_booking')
        except Exception as e:
            error_mg = "oops!!"
            messages.error(request, error_mg)
            return redirect('success_booking')
        
        
def plum_service_booking(request, pk):
    plum_service_data = {
        "plumbing_data": Plumbers.objects.get(pk=pk),
    }
    return render(request, "plum_serv_booking.html", plum_service_data)


def plumbing_service_booking(request):
    if request.method == "POST":
        try:
            booking_name = request.POST.get("name")
            booking_email = request.POST.get("email")
            booking_phone = request.POST.get("phone")
            booking_location = request.POST.get("location")
            booking_service = request.POST.get("service")
            booking_price = request.POST.get("price")
            booking_address = request.POST.get("address")
            booking_data = Plumbing_service_booking.objects.create(
                booking_name=booking_name,
                booking_email=booking_email,
                booking_phone=booking_phone,
                booking_location=booking_location,
                booking_service=booking_service,
                booking_price=booking_price,
                booking_address=booking_address,
            )
            booking_data.save()
            success_msg = "Successfully Booked"
            messages.success(request, success_msg)
            return redirect('success_booking')
        except Exception as e:
            error_mg = "oops!!"
            messages.error(request, error_mg)
            return redirect('success_booking')
