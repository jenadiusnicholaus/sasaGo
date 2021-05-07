from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import BookingForm
<<<<<<< HEAD
from .models import Service, Booking

=======
from .models import Vehicle, Bookings, BookedVehicle, CargoInfo
from django.contrib.auth import get_user_model

User = get_user_model()
>>>>>>> 2c2d5d29f535de50056b0f208a25d9c2f4407a63


def home(request):
    services = Service.objects.all()
    
    context = {
        'services': services
    }
<<<<<<< HEAD
    return render(request, 'home/home.html', context)


def book_service(request, id):
    services = Service.objects.get(id=id)
    if request.method == 'POST':
        print(request.POST)
        form = BookingForm(request.POST)
        booking = Booking()
        if form.is_valid():
            booking.pickup_location = form.cleaned_data['pickup_location']
            booking.destination = form.cleaned_data['destination']
            booking.package_size = form.cleaned_data['package_size']
            booking.phone = form.cleaned_data['phone']
            booking.booked_vehicle = form.cleaned_data['booked_vehicle']
            booking.booked_by = request.user
            booking.save()
            send_mail(
                    'A vehicle Has Been Booked', 
                    f"Please visit sasagoafrica Admin panel to see more details",
                    'ummasoft@gmail.com',['isayaelib@gmail.com'], fail_silently=False
                )
            return redirect('/')
        return redirect('book_service', id=id)

    context = {
         'data':services
     }
    return render(request, 'home/booking.html', context)
=======
    return render(request, 'home/home.html', context=context)


class VehicleDetails(View):
    def get(self, request, pk, format=None):
        # pk = self.kwargs.get('pk')
        # print(pk)
        queryset = get_object_or_404(Vehicle, pk=pk)
        context = {
            'vehicle_detail': queryset
        }
        template_name = 'home/vehicle_details.html'
        return render(request, template_name=template_name, context=context)


@login_required
def makeBooking(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    add_to_booking, created = BookedVehicle.objects.get_or_create(vehicle=vehicle, user=request.user)
    booking_qs = Bookings.objects.filter(user=request.user)
    if booking_qs.exists() and booking_qs.filter(vehicles__pk=vehicle.pk).exists():
        booking = booking_qs[0]
        if booking.vehicles.filter(vehicle__pk=vehicle.pk).exists():
            form = BookingForm(request.POST)
            if form.is_valid():

                cargo_from = form.cleaned_data.get('cargo_from')
                to = form.cleaned_data.get('to')
                fromAddress = form.cleaned_data.get('fromAddress')
                toAddress = form.cleaned_data.get('toAddress')
                region = form.cleaned_data.get('region')
                district = form.cleaned_data.get('district')
                town = form.cleaned_data.get('town')

                cargo_info = CargoInfo()

                cargo_info.user = request.user
                cargo_info.booking = booking
                cargo_info.vehicle = vehicle
                cargo_info.cargo_from = cargo_from
                cargo_info.to = to
                cargo_info.town = town
                cargo_info.from_Address = fromAddress
                cargo_info.to_Address = toAddress
                cargo_info.Region = region
                cargo_info.district = district
                cargo_info.save()

                messages.success(request, " Your Booking information is updated.")
                return redirect("/")
            else:

                return redirect("/")
        else:
            booking.vehicles.add(add_to_booking)
            messages.success(request, "You Booking is updated.")
            return redirect("/")
    else:
        booking = Bookings.objects.create(user=request.user)
        booking.vehicles.add(add_to_booking)

        form = BookingForm(request.POST)
        if form.is_valid():
            cargo_from = form.cleaned_data.get('cargo_from')
            to = form.cleaned_data.get('to')
            fromAddress = form.cleaned_data.get('fromAddress')
            toAddress = form.cleaned_data.get('toAddress')
            region = form.cleaned_data.get('region')
            district = form.cleaned_data.get('district')
            town = form.cleaned_data.get('town')

            CargoInfo.objects.create(
                user=request.user,
                booking=booking, cargo_from=cargo_from, to=to, town=town,
                from_Address=fromAddress, to_Address=toAddress,
                Region=region, district=district)

            messages.success(request, f"Your booking is done  .")
            return redirect("/")

        return redirect('/')
>>>>>>> 2c2d5d29f535de50056b0f208a25d9c2f4407a63
