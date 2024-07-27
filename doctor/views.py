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
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404



class VaccineViewSet(APIView):
   
    # serializer_class = PostSerializer

    # permission_classes = [IsAuthorOrReadOnly]
    
    def get(self, request, format=None):
        vaccines = Vaccine.objects.all()
        serializer = VaccineSerializer(vaccines, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = VaccineSerializer(data=request.data)
        serializer.created_by = request.user
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VaccineDetailViewSet(APIView):

    def get_object(self, pk):
        try:
            return Vaccine.objects.get(pk=pk)
        except Vaccine.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vaccine = self.get_object(pk)
        serializer = VaccineSerializer(vaccine)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        vaccine = self.get_object(pk)
        serializer = VaccineSerializer(vaccine, data=request.data)
        if serializer.is_valid():
            serializer.save(doctor=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vaccine = self.get_object(pk)
        vaccine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# class VaccineScheduleListCreate(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         user = request.user
#         if user.role == 'doctor':
#             schedules = VaccineSchedule.objects.filter(doctor=user)
#             serializer = VaccineScheduleSerializer(schedules, many=True)
#             return Response(serializer.data)
#         return Response(status=status.HTTP_403_FORBIDDEN)

#     def post(self, request, format=None):
#         serializer = VaccineScheduleSerializer(data=request.data)
#         serializer.doctor = request.user
#         if serializer.is_valid():
#             serializer.save(doctor=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class VaccineScheduleDetail(APIView):
#     permission_classes = [IsAuthenticated]

#     def get_object(self, pk):
#         try:
#             return VaccineSchedule.objects.get(pk=pk)
#         except VaccineSchedule.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         schedule = self.get_object(pk)
#         serializer = VaccineScheduleSerializer(schedule)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         schedule = self.get_object(pk, request.user)
#         serializer = VaccineScheduleSerializer(schedule, data=request.data)
#         if serializer.is_valid():
#             serializer.save(doctor=request.user)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         schedule = self.get_object(pk, request.user)
#         schedule.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
