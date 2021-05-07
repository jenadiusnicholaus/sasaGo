from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

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


class UserSignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    mobile = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class LoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField()
