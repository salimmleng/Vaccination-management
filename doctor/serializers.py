from rest_framework import serializers
from . import models
class VaccineSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Vaccine
        fields = '__all__'
        

class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = '__all__'
        