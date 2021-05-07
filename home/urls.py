from django.urls import path
<<<<<<< HEAD
from .views import home, book_service

urlpatterns = [
    path('', home, name='home'),
    path('service/<int:id>/',book_service,name='book_service')
=======
from .views import home, VehicleDetails, makeBooking

urlpatterns = [
    path('', home, name='home'),
    path('vehicle_details/<int:pk>/', VehicleDetails.as_view(),
         name='vehicle_details'),
    path('booking/<int:pk>/', makeBooking, name='make_booking')
>>>>>>> 2c2d5d29f535de50056b0f208a25d9c2f4407a63
]
