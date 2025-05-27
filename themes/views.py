from django.shortcuts import render
from . models import Contact
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        msg = request.POST.get('msg')
        contact_data = Contact.objects.create(name=name, email=email, phone=phone, service=service, message=msg)
        contact_data.save()
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')