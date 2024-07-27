# from django.db import models
# from accounts.models import CustomUser
# # Create your models here.

# class Vaccine(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()
#     doctor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
#     schedule_date = models.DateTimeField()


# class Doctor(models.Model):
#     image = models.ImageField(upload_to="doctor/images/")
#     name = models.CharField(max_length=50)
#     specialist = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.name


# mod

from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import date
CustomUser = get_user_model()


class Vaccine(models.Model):
    image = models.ImageField(upload_to="doctor/images/",default='default.jpg')
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=100,default='default-manufacturer')
    batch_number = models.CharField(max_length=100,default='default-batch-number')
    expiry_date =  models.DateField(default=date(2024, 12, 31)) 
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class VaccineSchedule(models.Model):
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, related_name='schedules')
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vaccine_schedules')
    patient_name = models.CharField(max_length=100,default="anything")
    scheduled_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return f"{self.vaccine.name} on {self.scheduled_date}"



