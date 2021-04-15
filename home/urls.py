from django.urls import path
from .views import home, VehicleDetails

urlpatterns = [
    path('', home, name='home'),
    path('vehicle_details/<int:pk>/', VehicleDetails.as_view(),
         name='vehicle_details')
]
