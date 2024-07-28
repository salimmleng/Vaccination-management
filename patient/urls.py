from django.urls import path
from .views import BookFirstDoseView,AvailableDatesView

urlpatterns = [
    path('book-dose/',BookFirstDoseView.as_view(), name='book-dose'),
    path('available-dates/', AvailableDatesView.as_view(), name='available-dates'),
]



