from django.shortcuts import render
from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import DoseBooking
from doctor.models import VaccineSchedule 
from .serializers import DoseBookingSerializer, AvailableDatesSerializer
from datetime import timedelta

from .import serializers
from .import models 


class PatientViewSet(viewsets.ModelViewSet):

    queryset = models.Patient.objects.all() 
    serializer_class = serializers.PatientSerializer




class AvailableDatesView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # For demonstration, we're using a static list of dates.
        # In a real-world scenario, this could be fetched from the database.
        return VaccineSchedule.objects.all()

    def list(self, request, *args, **kwargs):
        available_dates = ["2024-07-23", "2024-07-24", "2024-07-25"]
        serializer = AvailableDatesSerializer({"available_dates": available_dates})
        return Response(serializer.data)

class DoseBookingView(generics.CreateAPIView):
    queryset = DoseBooking.objects.all()
    serializer_class = DoseBookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

