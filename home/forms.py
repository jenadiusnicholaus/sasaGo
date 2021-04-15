from django import forms


class BookingForm(forms.Form):
    cargo_from = forms.CharField()
    to = forms.CharField()
    fromAddress = forms.CharField()
    toAddress = forms.CharField()
    region = forms.CharField()
    district = forms.CharField()
    town = forms.CharField()
