from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AvailableHospitalViewSet, AvailableDatesViewSet, DoseViewSet

router = DefaultRouter()
router.register(r'available_hospitals', AvailableHospitalViewSet)
router.register(r'available_dates', AvailableDatesViewSet)
router.register(r'doses', DoseViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
