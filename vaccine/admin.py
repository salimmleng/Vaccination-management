from django.contrib import admin
from .models import Dose,AvailableDates,AvailableHospital
# Register your models here.

admin.site.register(Dose)
admin.site.register(AvailableHospital)
admin.site.register(AvailableDates)

