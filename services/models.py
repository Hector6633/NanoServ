from django.db import models
from auditlog.registry import auditlog

# Create your models here.
class Electricians(models.Model):
    service_img = models.ImageField()
    service_name = models.CharField(max_length=50)
    service_price = models.CharField(max_length=5)
    service_desc = models.TextField()

    def __str__(self) -> str:
        return self.service_name
    
auditlog.register(Electricians)


class Plumbers(models.Model):
    service_img = models.ImageField()
    service_name = models.CharField(max_length=50)
    service_price = models.CharField(max_length=5)
    service_desc = models.TextField()

    def __str__(self) -> str:
        return self.service_name
    
auditlog.register(Plumbers)


class SmartTv(models.Model):
    service_img = models.ImageField()
    service_name = models.CharField(max_length=50)
    service_price = models.CharField(max_length=5)
    service_desc = models.TextField()

    def __str__(self) -> str:
        return self.service_name

auditlog.register(SmartTv)


class Electrical_service_booking(models.Model):
    booking_name = models.CharField(max_length=50, null=False)
    booking_email = models.EmailField(blank=False, null=False)
    booking_phone = models.CharField(max_length=10, blank=False, null=False)
    booking_location = models.CharField(max_length=50, null=False)
    booking_service = models.CharField(max_length=50, null=False)
    booking_price = models.CharField(max_length=5, null=False)
    booking_address = models.TextField(null=False)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.booking_name
    

class Plumbing_service_booking(models.Model):
    booking_name = models.CharField(max_length=50, null=False)
    booking_email = models.EmailField(blank=False, null=False)
    booking_phone = models.CharField(max_length=10, blank=False, null=False)
    booking_location = models.CharField(max_length=50, null=False)
    booking_service = models.CharField(max_length=50, null=False)
    booking_price = models.CharField(max_length=5, null=False)
    booking_address = models.TextField(null=False)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.booking_name


class smartTv_service_booking(models.Model):
    booking_name = models.CharField(max_length=50, null=False)
    booking_email = models.EmailField(blank=False, null=False)
    booking_phone = models.CharField(max_length=10, blank=False, null=False)
    booking_location = models.CharField(max_length=50, null=False)
    booking_service = models.CharField(max_length=50, null=False)
    booking_price = models.CharField(max_length=5, null=False)
    booking_address = models.TextField(null=False)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.booking_name
