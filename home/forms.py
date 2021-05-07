from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from home.models import Booking


class BookingForm(forms.Form):
    pickup_location = forms.CharField()
    destination = forms.CharField()
    booked_vehicle = forms.CharField()
    package_size = forms.CharField()
    phone = forms.CharField()
    
    class Meta:
        model = Booking
        fields = '__all__'


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
