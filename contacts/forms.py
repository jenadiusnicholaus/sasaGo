from django  import forms
from .models import Contact

class contactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    phone = forms.CharField()
    message = forms.CharField()

    class Meta:
        model = Contact
        fields =  '__all__'