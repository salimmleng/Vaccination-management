from django.db import models
from accounts.models import CustomUser
from doctor.models import VaccineSchedule
# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(CustomUser ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="patient/images/")
    mobile_no = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}" 
    

# mod

class DoseBooking(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='dose_bookings')
    vaccine_schedule = models.ForeignKey(VaccineSchedule, on_delete=models.CASCADE)
    first_dose_date = models.DateField()
    second_dose_date = models.DateField()
    booked_at = models.DateTimeField(auto_now_add=True)


    