from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


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



class Service(models.Model):
    service_type =  models.CharField(max_length=100, choices=SERVICE_TYPE)
    details = models.TextField()
    service_icon = models.CharField(max_length=100,choices=ICON_LABEL_CHOICE)

    def __str__(self):
        return self.service_type


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
