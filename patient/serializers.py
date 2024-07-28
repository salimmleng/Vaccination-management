from rest_framework import serializers
from accounts.models import CustomUser
from rest_framework import serializers
from datetime import timedelta

from .import models

# serializers.py in patient app
from rest_framework import serializers
from .models import Dose

class DoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dose
        fields = ['id', 'user', 'vaccine', 'dose_number', 'scheduled_date', 'administered_date']
        read_only_fields = ['dose_number']

