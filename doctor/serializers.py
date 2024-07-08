from rest_framework import serializers
from . import models
class VaccineSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Vaccine
        fields = '__all__'
        