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
        fields = ['id', 'name', 'created_at', 'created_by']

class VaccineScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccineSchedule
        fields = ['id', 'vaccine', 'date', 'doctor', 'notes']
