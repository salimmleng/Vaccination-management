from rest_framework import serializers
from accounts.models import CustomUser
from rest_framework import serializers
from datetime import timedelta

# serializers.py in patient app
from rest_framework import serializers
from .models import Dose,AvailableHospital,AvailableDates

class DoseSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    vaccine = serializers.StringRelatedField(many=False)
    vaccine_center = serializers.StringRelatedField(many=False)
    class Meta:
        model = Dose
        fields ='__all__'

        
class AvailableHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableHospital
        fields ='__all__'

class AvailableDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableDates
        fields ='__all__'
