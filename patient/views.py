from django.shortcuts import render
from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import Dose
from .serializers import DoseSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status

from .import serializers
from .import models 


# views.py in patient app
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Dose
from .serializers import DoseSerializer
from datetime import date
from datetime import timedelta,datetime
from rest_framework.exceptions import ValidationError
from doctor.models import Vaccine


class BookFirstDoseView(generics.CreateAPIView):
    queryset = Dose.objects.all()
    serializer_class = DoseSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        # if user.is_anonymous:
        #     raise ValidationError("User must be authenticated to book a dose.")
        
        vaccine_id = self.request.data.get('vaccine')
        scheduled_date_str = self.request.data.get('scheduled_date')

        try:
            vaccine = Vaccine.objects.get(id=vaccine_id)
        except Vaccine.DoesNotExist:
            raise ValidationError("Invalid vaccine ID.")

        # Convert scheduled_date_str to a date object
        try:
            scheduled_date = datetime.strptime(scheduled_date_str, '%Y-%m-%d').date()
        except ValueError:
            raise ValidationError("Invalid date format. Use 'YYYY-MM-DD'.")

        # Check if the first dose already exists for the user and vaccine
        if Dose.objects.filter(user=user, vaccine=vaccine, dose_number=1).exists():
            raise ValidationError("First dose already booked for this vaccine.")

        # Save the first dose
        first_dose = serializer.save(
            user=user,
            vaccine=vaccine,
            dose_number=1,
            scheduled_date=scheduled_date
        )

        # Automatically schedule the second dose 21 days later
        second_dose_date = scheduled_date + timedelta(days=21)
        Dose.objects.create(
            user=user,
            vaccine=vaccine,
            dose_number=2,
            scheduled_date=second_dose_date
        )
        return first_dose


class AvailableDatesView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        today = date.today()
        available_dates = [today + timedelta(days=i) for i in range(30)]  # Next 30 days
        available_dates = [d.isoformat() for d in available_dates]  # Convert to string format
        return Response(available_dates)
    



    

