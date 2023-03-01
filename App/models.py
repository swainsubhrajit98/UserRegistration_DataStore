from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    dob=models.DateField()
    phone=models.IntegerField()
    address=models.CharField(max_length=55)
    country=models.CharField(max_length=55)
    state=models.CharField(max_length=55)
    zip=models.IntegerField()
    
    def __str__(self):
        return self.name
