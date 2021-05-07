from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import BookingForm
from .models import Service, Booking



def home(request):
    services = Service.objects.all()

    context = {
        'services': services
    }
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









