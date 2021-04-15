import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

SERVICE_TYPE = (
    ('motoboy', 'Motoboy'),
    ('mintruck', 'Min Truck'),
    ('tuck', 'Truck')
)

ICON_LABEL_CHOICE = (
    ('motorcycle', 'motorcycle'),
    ('shuttle-van', 'shuttle-van'),
    ('truck-moving', 'truck-moving')
)


class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle_type = models.CharField(choices=SERVICE_TYPE, max_length=20)
    icon_label = models.CharField(max_length=20, choices=ICON_LABEL_CHOICE, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        verbose_name = 'Vehicles'

    def __str__(self):
        return str(self.vehicle_type)


class BookedVehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        verbose_name_plural = 'Booked Vehicles'

    def __str__(self):
        return str(self.vehicle.vehicle_type)


class Bookings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booked_by')
    vehicles = models.ManyToManyField(BookedVehicle, related_name='List_booking', )
    created_at = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        verbose_name_plural = 'Bookings'

    def __str__(self):
        # return str(self.user)
        for vehicle in self.vehicles.all():
            return f'{self.user} booked {str(vehicle.vehicle)}'


class CargoInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_user_info', null=True)
    booking=models.ForeignKey(Bookings, on_delete=models.SET_NULL, null=True)
    cargo_from = models.CharField(max_length=200, null=True)
    to = models.CharField(max_length=200, null=True)
    from_Address = models.CharField(max_length=200, null=True)
    to_Address = models.CharField(max_length=200, null=True)
    Region = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    town = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        verbose_name_plural = 'Cargo information'

    def __str__(self):
        return str(self.booking)
