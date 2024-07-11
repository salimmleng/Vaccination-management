from django.urls import path
from .views import AvailableDatesView, DoseBookingView

urlpatterns = [
    path('available-dates/', AvailableDatesView.as_view(), name='available-dates'),
    path('book-dose/', DoseBookingView.as_view(), name='book-dose'),
]
