from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .import serializers
from .import models
# Create your views here.

class VaccineViewSet(viewsets.ModelViewSet):
    queryset = models.Vaccine.objects.all()
    serializer_class = serializers.VaccineSerializers

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializers