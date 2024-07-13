# from django.shortcuts import render
# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from .import serializers
# from .import models
# # Create your views here.

# class VaccineViewSet(viewsets.ModelViewSet):
#     queryset = models.Vaccine.objects.all()
#     serializer_class = serializers.VaccineSerializers

# class DoctorViewSet(viewsets.ModelViewSet):
#     queryset = models.Doctor.objects.all()
#     serializer_class = serializers.DoctorSerializers



# mod 

from rest_framework import viewsets, permissions
from .models import Vaccine, VaccineSchedule
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializers import VaccineSerializer, VaccineScheduleSerializer


class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class VaccineScheduleViewSet(viewsets.ModelViewSet):
    queryset = VaccineSchedule.objects.all()
    serializer_class = VaccineScheduleSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.role == 'doctor':
            return self.queryset.filter(doctor=user)
        return self.queryset.none()

    