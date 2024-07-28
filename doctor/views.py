

from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .serializers import VaccineSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Vaccine


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

