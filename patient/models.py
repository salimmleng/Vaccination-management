from django.db import models
from django.conf import settings
from doctor.models import Vaccine
from datetime import timedelta, date

class Dose(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    dose_number = models.IntegerField()  # 1 for first dose, 2 for second dose
    scheduled_date = models.DateField()
    administered_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - Dose {self.dose_number} of {self.vaccine.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.dose_number == 1 and not Dose.objects.filter(user=self.user, dose_number=2, vaccine=self.vaccine).exists():
            self.schedule_second_dose()

    def schedule_second_dose(self):
        second_dose_date = self.scheduled_date + timedelta(days=21)  # Adjust the days as per your requirement
        Dose.objects.create(
            user=self.user,
            vaccine=self.vaccine,
            dose_number=2,
            scheduled_date=second_dose_date
        )


