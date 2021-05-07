from django.contrib import admin
from home.models import Service, Booking
from django.contrib.auth.models import Group

admin.site.unregister(Group)

admin.site.register(Service)
admin.site.register(Booking)


