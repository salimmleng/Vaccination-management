# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import AvailableHospitalViewSet, AvailableDatesViewSet, DoseViewSet

# router = DefaultRouter()
# router.register(r'available_hospitals', AvailableHospitalViewSet)
# router.register(r'available_dates', AvailableDatesViewSet)
# router.register(r'doses', DoseViewSet, basename='dose')

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]

# urls.py
from django.urls import path
from .views import DoseListCreateView, DoseDetailView, AvailableHospitalListView, AvailableDatesListView

urlpatterns = [
    path('api/doses/', DoseListCreateView.as_view(), name='dose-list-create'),
    path('api/doses/<int:pk>/', DoseDetailView.as_view(), name='dose-detail'),
    path('api/available_hospitals/', AvailableHospitalListView.as_view(), name='available-hospitals-list'),
    path('api/available_dates/', AvailableDatesListView.as_view(), name='available-dates-list'),
]

