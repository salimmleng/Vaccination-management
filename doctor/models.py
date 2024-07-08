from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    doctor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    schedule_date = models.DateTimeField()
