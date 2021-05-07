from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from sasaGo import settings

SERVICE_TYPE = (
    ('Boda Boda', 'Boda Boda'),
    ('Van/Kirikuu', 'Van/Kirikuu'),
    ('Truck', 'Truck')
)

ICON_LABEL_CHOICE = (
    ('motorcycle', 'motorcycle'),
    ('shuttle-van', 'shuttle-van'),
    ('truck-moving', 'truck-moving')
)

<<<<<<< HEAD
class Service(models.Model):
    service_type =  models.CharField(max_length=100, choices=SERVICE_TYPE)
    details = models.TextField()
    service_icon = models.CharField(max_length=100,choices=ICON_LABEL_CHOICE)

    def __str__(self):
        return self.service_type
=======
user = settings.AUTH_USER_MODEL
class Vehicle(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    vehicle_type = models.CharField(choices=SERVICE_TYPE, max_length=20)
    icon_label = models.CharField(max_length=20, choices=ICON_LABEL_CHOICE, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        verbose_name = 'Vehicles'

    def __str__(self):
        return str(self.vehicle_type)


class BookedVehicle(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)

    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='users')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        verbose_name_plural = 'Booked Vehicles'

    def __str__(self):
        return str(self.vehicle.vehicle_type)


class Bookings(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='booked_by')
    vehicles = models.ManyToManyField(BookedVehicle, related_name='List_booking', )
    created_at = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        verbose_name_plural = 'Bookings'

    def __str__(self):
        # return str(self.user)
        for vehicle in self.vehicles.all():
            return f'{self.user} booked {str(vehicle.vehicle)}'


class CargoInfo(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='booking_user_info', null=True)
    booking = models.ForeignKey(Bookings, on_delete=models.SET_NULL, null=True)
    cargo_from = models.CharField(max_length=200, null=True)
    to = models.CharField(max_length=200, null=True)
    from_Address = models.CharField(max_length=200, null=True)
    to_Address = models.CharField(max_length=200, null=True)
    Region = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    town = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)
>>>>>>> 2c2d5d29f535de50056b0f208a25d9c2f4407a63


class Booking(models.Model):
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    booked_vehicle = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=100)
    package_size = models.CharField(max_length=100, blank=True, null=True)
    destination = models.CharField(max_length=100,)
    phone = models.CharField(max_length=100)
    booked_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.booked_vehicle
