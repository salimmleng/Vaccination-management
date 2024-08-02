from rest_framework import viewsets
from .models import AvailableHospital, AvailableDates, Dose
from .serializers import AvailableHospitalSerializer, AvailableDatesSerializer, DoseSerializer

class AvailableHospitalViewSet(viewsets.ModelViewSet):
    queryset = AvailableHospital.objects.all()
    serializer_class = AvailableHospitalSerializer

class AvailableDatesViewSet(viewsets.ModelViewSet):
    queryset = AvailableDates.objects.all()
    serializer_class = AvailableDatesSerializer

class DoseViewSet(viewsets.ModelViewSet):
    queryset = Dose.objects.all()
    serializer_class = DoseSerializer


    