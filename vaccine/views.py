from rest_framework import viewsets
from .models import AvailableHospital, AvailableDates, Dose
from .serializers import AvailableHospitalSerializer, AvailableDatesSerializer, DoseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from datetime import timedelta,datetime

# class AvailableHospitalViewSet(viewsets.ModelViewSet):
#     queryset = AvailableHospital.objects.all()
#     serializer_class = AvailableHospitalSerializer

# class AvailableDatesViewSet(viewsets.ModelViewSet):
   
#     serializer_class = AvailableDatesSerializer

# class DoseViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = DoseSerializer
#     queryset = Dose.objects.all()
    
#     def get_queryset(self):
#         return Dose.objects.filter(user=self.request.user)


class DoseListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        doses = Dose.objects.filter(user=request.user)
        serializer = DoseSerializer(doses, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()

        first_dose_date_id = data.get('firstDose_date_id')
        if first_dose_date_id:
            try:
                first_dose_date_obj = AvailableDates.objects.get(id=first_dose_date_id)
                
                # Calculate the second dose date
                second_dose_date_value = first_dose_date_obj.date + timedelta(days=21)
                
                # Get or create the second dose date object
                second_dose_date_obj, created = AvailableDates.objects.get_or_create(date=second_dose_date_value)
                
                # Set the date objects' IDs in the data
                data['firstDose_date_id'] = first_dose_date_obj.id
                data['secondDose_date_id'] = second_dose_date_obj.id
            except AvailableDates.DoesNotExist:
                return Response({"error": "Invalid date ID for firstDose_date."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "firstDose_date_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DoseSerializer(data=data)
        if serializer.is_valid():
            try:
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DoseDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Dose.objects.get(pk=pk, user=user)
        except Dose.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dose = self.get_object(pk, request.user)
        serializer = DoseSerializer(dose)
        return Response(serializer.data)

    def put(self, request, pk):
        dose = self.get_object(pk, request.user)
        serializer = DoseSerializer(dose, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dose = self.get_object(pk, request.user)
        dose.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AvailableHospitalListView(APIView):
    def get(self, request):
        hospitals = AvailableHospital.objects.all()
        serializer = AvailableHospitalSerializer(hospitals, many=True)
        return Response(serializer.data)

class AvailableDatesListView(APIView):
    def get(self, request):
        dates = AvailableDates.objects.all()
        serializer = AvailableDatesSerializer(dates, many=True)
        return Response(serializer.data)
    
