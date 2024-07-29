from django.db import models
from django.conf import settings
from doctor.models import Vaccine
from datetime import timedelta, date

class Dose(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    dose_number = models.IntegerField()  # 1 for first dose, 2 for second dose
    scheduled_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'vaccine', 'dose_number')

    def __str__(self):
        return f"{self.user} - {self.vaccine.name} (Dose {self.dose_number})"


