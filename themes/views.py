from django.shortcuts import render, redirect
from . models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            service = request.POST.get('service')
            msg = request.POST.get('msg')
            contact_data = Contact.objects.create(name=name, email=email, phone=phone, service=service, message=msg)
            contact_data.save()
            success_msg = 'Successfully submitted'
            messages.success(request, success_msg)
            return redirect('contact')
        except Exception as e:
            error_msg = 'Server unreachable'
            messages.error(request, error_msg)
            return redirect('contact')
    return render(request, 'contact.html')
