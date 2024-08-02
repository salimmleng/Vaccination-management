from django.db import models
from django.conf import settings
from doctor.models import Vaccine

VACCINE_STATUS = [
    ('Completed','Completed'),
    ('Pending','Pending'),
]

class AvailableHospital(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AvailableDates(models.Model):
    date = models.DateField()
    
    def __str__(self):
        return self.date.strftime('%Y-%m-%d')


class Dose(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    dose_number = models.IntegerField() 
    vaccine_status = models.CharField(choices=VACCINE_STATUS,max_length=20,default='Pending')
    vaccine_center = models.ForeignKey(AvailableHospital, on_delete=models.CASCADE)
    date = models.ForeignKey(AvailableDates, on_delete=models.CASCADE,null=True,blank=True)
    mobile_no = models.CharField(max_length=12,default=00)
    cancel = models.BooleanField(default=False)
   
