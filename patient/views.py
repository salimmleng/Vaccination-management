from django.shortcuts import render
from django.shortcuts import render,redirect
from rest_framework import viewsets
# Create your views here.

from .import serializers
from .import models 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from accounts.models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login,logout


# for sending email 
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



class PatientViewSet(viewsets.ModelViewSet):

    queryset = models.Patient.objects.all() # data asbe
    serializer_class = serializers.PatientSerializer # data j



class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print('Token', token)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print('Uid',uid)
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            email_subject = "confirm your email"
            email_body = render_to_string('confirm_email.html',{'confirm_link': confirm_link})

            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)



def activate(request,uid64,token):

    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = CustomUser._default_manager.get(pk=uid)
    except(CustomUser.DoesNotExist):

        user  = None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect("login")
    else:
        return redirect("register")
    



class UserLoginApiView(APIView):

    def post(self,request):

        serializer = serializers.UserloginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username,password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request,user)
                return Response({"token": token.key, 'user_id': user.id})
            else:
               
                return redirect('login')
            
        else:
            return Response(serializer.errors)
        
