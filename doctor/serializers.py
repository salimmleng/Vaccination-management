# from rest_framework import serializers
# from . import models
# class VaccineSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = models.Vaccine
#         fields = '__all__'
        

# class DoctorSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = models.Doctor
#         fields = '__all__'    



# mod

from rest_framework import serializers
from .models import Vaccine, VaccineSchedule

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = ['id', 'image', 'name', 'manufacturer','batch_number','expiry_date', 'created_at', 'created_by']
        read_only_fields = ['created_by',]


class VaccineScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccineSchedule
        fields = ['id', 'patient_name','doctor','created_at', 'scheduled_date']  # Example fields; adjust as per your model
        read_only_fields = ['doctor']  # If doctor_name should be read-only