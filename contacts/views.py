from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact
from .forms import contactForm
# Create your views here.
def send_message(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        contact = Contact()
        if form.is_valid():
            contact.name = form.cleaned_data['name']
            contact.email = form.cleaned_data['email']
            contact.phone = form.cleaned_data['phone']
            contact.message = form.cleaned_data['message']
            contact.save()
            send_mail(
                    'New message from customers', 
                    f"Please visit your admin panel site to the message",
                    'ummasoft@gmail.com',['isayaelib@gmail.com'], fail_silently=False
                )
            messages.success(request, f"Your Message has been sent successful!")
            return redirect('/')
        messages.error(request, f"Your Message has not been sent!")
        return redirect('/')