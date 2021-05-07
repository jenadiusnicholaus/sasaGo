from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookingForm(forms.Form):
    cargo_from = forms.CharField()
    to = forms.CharField()
    fromAddress = forms.CharField()
    toAddress = forms.CharField()
    region = forms.CharField()
    district = forms.CharField()
    town = forms.CharField()



