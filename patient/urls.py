from django.urls import path
from .views import AvailableDatesView, BookDoseView

urlpatterns = [
    path('available-dates/', AvailableDatesView.as_view(), name='available-dates'),
    path('book-dose/',BookDoseView.as_view(), name='book-dose'),
]



