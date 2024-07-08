from rest_framework import serializers
from accounts.models import CustomUser

from .import models

class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Patient
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
 
    class Meta:
        model = CustomUser 
        fields = ['username','first_name','last_name','email','nid','password','confirm_password']

    def save(self):
        username = self.validated_data["username"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]
        email = self.validated_data["email"]
        password = self.validated_data["password"]
        confirm_password = self.validated_data["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError({'error': "password doesn't match"})
        if CustomUser.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error': "Email already exists"})
        
        account = CustomUser(username=username,first_name=first_name,last_name=last_name,email=email)

        account.set_password(password)
        account.is_active = False
        account.save()
        return account


class UserloginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
