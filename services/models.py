from django.db import models


# Create your models here.
class Electricians(models.Model):
    service_img = models.ImageField()
    service_name = models.CharField(max_length=50)
    service_price = models.CharField(max_length=5)
    service_desc = models.TextField()

    def __str__(self) -> str:
        return self.service_name


class Plumbers(models.Model):
    service_img = models.ImageField()
    service_name = models.CharField(max_length=50)
    service_price = models.CharField(max_length=5)
    service_desc = models.TextField()

    def __str__(self) -> str:
        return self.service_name


class SmartTv(models.Model):
    service_img = models.ImageField()
    service_name = models.CharField(max_length=50)
    service_price = models.CharField(max_length=5)
    service_desc = models.TextField()

    def __str__(self) -> str:
        return self.service_name


class Electrical_service_booking(models.Model):
    booking_name = models.CharField(max_length=50, null=False)
    booking_email = models.EmailField(blank=False)
    booking_phone = models.CharField(max_length=10, blank=False)
    booking_location = models.CharField(max_length=50)
    booking_service = models.CharField(max_length=50)
    booking_price = models.CharField(max_length=5)
    booking_address = models.TextField()
    
    def __str__(self) -> str:
        return self.booking_name
    
    
class Plumbing_service_booking(models.Model):
    booking_name = models.CharField(max_length=50, null=False)
    booking_email = models.EmailField(blank=False)
    booking_phone = models.CharField(max_length=10, blank=False)
    booking_location = models.CharField(max_length=50)
    booking_service = models.CharField(max_length=50)
    booking_price = models.CharField(max_length=5)
    booking_address = models.TextField()
    
    def __str__(self) -> str:
        return self.booking_name
    
    
class smartTv_service_booking(models.Model):
    booking_name = models.CharField(max_length=50, null=False)
    booking_email = models.EmailField(blank=False)
    booking_phone = models.CharField(max_length=10, blank=False)
    booking_location = models.CharField(max_length=50)
    booking_service = models.CharField(max_length=50)
    booking_price = models.CharField(max_length=5)
    booking_address = models.TextField()
    
    def __str__(self) -> str:
        return self.booking_name
