# from rest_framework import serializers
# from accounts.models import CustomUser
# from rest_framework import serializers
# from datetime import timedelta

# # serializers.py in patient app
# from rest_framework import serializers
# from .models import Dose,AvailableHospital,AvailableDates

# class DoseSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField(many=False)
#     vaccine = serializers.StringRelatedField(many=False)
#     vaccine_center = serializers.StringRelatedField(many=False)
#     firstDose_date = serializers.SlugRelatedField(slug_field='date', queryset=AvailableDates.objects.all())
#     secondDose_date = serializers.SlugRelatedField(slug_field='date', queryset=AvailableDates.objects.all(), required=False)

#     class Meta:
#         model = Dose
#         fields = '__all__'

        
# class AvailableHospitalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AvailableHospital
#         fields ='__all__'

# class AvailableDatesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AvailableDates
#         fields ='__all__'


from rest_framework import serializers
from .models import Dose, AvailableDates, AvailableHospital
from doctor.models import Vaccine
from accounts.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','first_name','nid']

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = ['id', 'name']

class AvailableDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableDates
        fields = ['id', 'date']

class AvailableHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableHospital
        fields = ['id', 'name']

class DoseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    vaccine = VaccineSerializer(read_only=True)
    vaccine_center = AvailableHospitalSerializer(read_only=True)
    firstDose_date = AvailableDatesSerializer(read_only=True)
    secondDose_date = AvailableDatesSerializer(read_only=True)

    vaccine_id = serializers.PrimaryKeyRelatedField(
        queryset=Vaccine.objects.all(), source='vaccine', write_only=True)
    vaccine_center_id = serializers.PrimaryKeyRelatedField(
        queryset=AvailableHospital.objects.all(), source='vaccine_center', write_only=True)
    firstDose_date_id = serializers.PrimaryKeyRelatedField(
        queryset=AvailableDates.objects.all(), source='firstDose_date', write_only=True)
    
    secondDose_date_id = serializers.PrimaryKeyRelatedField(
        queryset=AvailableDates.objects.all(), source='secondDose_date', write_only=True)

    class Meta:
        model = Dose
        fields = '__all__'
