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
CustomUser = get_user_model()

class Vaccine(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class VaccineSchedule(models.Model):
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vaccine_schedules')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self):
        return f"{self.vaccine.name} on {self.date}"
