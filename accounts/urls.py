# modified

from django.urls import path
from .views import UserRegistrationAPIView, UserProfileAPIView, ChangePasswordAPIView,UserLoginApiView,UserLogoutApiView,activate

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutApiView.as_view(), name='logout'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('activate/<uid64>/<token>/', activate, name='activate'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='change_password'),
]
