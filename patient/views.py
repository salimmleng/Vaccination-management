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
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status

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



# class DoseBookingView(generics.CreateAPIView):
#     queryset = DoseBooking.objects.all()
#     serializer_class = DoseBookingSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(patient=self.request.user)

class BookDoseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        dose_bookings = DoseBooking.objects.filter(patient=user)
        serializer = DoseBookingSerializer(dose_bookings, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data.copy()
        data['patient'] = user.id

        serializer = DoseBookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Dose booking request sent.", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


