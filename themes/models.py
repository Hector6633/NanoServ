from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    service = models.CharField(max_length=50)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name