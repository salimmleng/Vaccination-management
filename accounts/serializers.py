from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    ROLES=[
        ('patient','Patient'),
        ('doctor','Doctor'),
    ]
    role = serializers.ChoiceField(choices=ROLES)
    nid = serializers.CharField(unique=True)
    license_number = serializers.CharField(required=False)

    def validate_nid(self, data):
        if User.objects.filter(nid=data).exists():
            raise serializers.ValidationError("A user already exists")
        return data

        

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['role'] = self.validated_data.get('role', '')
        data['nid'] = self.validated_data.get('nid', '')
        print('Role selected:',data['role'])
        return data

    def save(self, request):
        user = super().save(request)
        user.role = self.cleaned_data.get('role')
        user.nid = self.cleaned_data.get('nid')
        user.save()
        return user
