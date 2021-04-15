from django.contrib import admin

# Register your models here.
from .models import Vehicle, BookedVehicle, Bookings, CargoInfo

admin.site.register(Vehicle)
admin.site.register(BookedVehicle)
admin.site.register(Bookings)
admin.site.register(CargoInfo)
