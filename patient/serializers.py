from rest_framework import serializers
from accounts.models import CustomUser
from rest_framework import serializers
from .models import DoseBooking
from doctor.models import VaccineSchedule
from datetime import timedelta

from .import models

class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Patient
        fields = '__all__'


class DoseBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoseBooking
        fields = ['id', 'patient', 'vaccine_schedule', 'first_dose_date', 'second_dose_date', 'booked_at']
        read_only_fields = ['second_dose_date', 'booked_at']

    def validate_first_dose_date(self, value):
        # Add any validation logic for the first dose date if necessary
        return value

    def create(self, validated_data):
        first_dose_date = validated_data['first_dose_date']
        validated_data['second_dose_date'] = first_dose_date + timedelta(days=28)  # Automatically set the second dose date
        return super().create(validated_data)

class AvailableDatesSerializer(serializers.Serializer):
    available_dates = serializers.ListField(
        child=serializers.DateField()
    )

