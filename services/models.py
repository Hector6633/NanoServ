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