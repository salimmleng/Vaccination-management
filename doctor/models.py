from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    doctor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    schedule_date = models.DateTimeField()


class Doctor(models.Model):
    image = models.ImageField(upload_to="doctor/images/")
    name = models.CharField(max_length=50)
    specialist = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
