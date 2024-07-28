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
from datetime import timedelta


class BookFirstDoseView(generics.CreateAPIView):
    queryset = Dose.objects.all()
    serializer_class = DoseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, dose_number=1)

class AvailableDatesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        today = date.today()
        available_dates = [today + timedelta(days=i) for i in range(30)]  # Next 30 days
        return Response(available_dates, status=status.HTTP_200_OK)
    


