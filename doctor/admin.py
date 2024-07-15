from django.contrib import admin
from .models import VaccineSchedule,Vaccine
# Register your models here.
admin.site.register(Vaccine)
admin.site.register(VaccineSchedule)