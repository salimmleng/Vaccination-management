from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter()

router.register('vaccine', views.VaccineViewSet)
router.register('doctor_list', views.DoctorViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

