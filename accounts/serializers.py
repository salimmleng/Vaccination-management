from rest_framework import serializers
from .models import CustomUser, PatientProfile, DoctorProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'nid']

class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = '__all__'

class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    role = serializers.ChoiceField(choices=CustomUser.ROLES)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'role', 'nid']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        role = self.validated_data['role']
        nid = self.validated_data['nid']

        if password != confirm_password:
            raise serializers.ValidationError({'error': "Passwords don't match"})
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email already exists"})
        if CustomUser.objects.filter(nid=nid).exists():
            raise serializers.ValidationError({'error': "NID already exists"})

        account = CustomUser(username=username, first_name=first_name, last_name=last_name, email=email, role=role, nid=nid)
        account.set_password(password)
        account.is_active = False
        account.save()

        if role == 'patient':
            PatientProfile.objects.create(user=account)
        elif role == 'doctor':
            DoctorProfile.objects.create(user=account)

        return account

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
