from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.views import View
# from authentication.models import User
from sasaGo import settings
from .forms import *

from django.contrib.auth import get_user_model

User = get_user_model()


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        print(form.data)
        messages.warning(request, "form is not valid.")
    form = NewUserForm
    return redirect('/')


def login_request(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    LoginForm()
    return redirect('/')


class UserSignUp(View):
    def get(self, *args, **kwargs):
        pass
        # let's pass here for now
        # context = {}
        # form = NewUserForm(self.request.POST or None)
        # context['form'] = form
        # return render(self.request, 'authentication/sign_up.html', context)

    def post(self, request, *args, **kwargs):
        form = UserSignUpForm(self.request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            mobile = form.cleaned_data.get('mobile')

            # print(username)
            # print(email)
            # print(password)
            # print(mobile)

            # cheking for passwords matching
            if password != password2:
                messages.warning(self.request, "password doesn't match")
                # For this we need toredirect to register page if there
                return redirect('/')

            if not (User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists()):
                User.objects.create_user(email, password, username=username , is_active=True)
                # it going to be used later in the email sending
                user = User.objects.get(username=username, email=email)
                # TODO send email address to activate a user if you want it to
                messages.success(self.request, f'Registered successfully now')
                return redirect('/')
            else:
                messages.warning(self.request, 'Looks like a username with that email or password already exists')
                return redirect("/")
        else:
            # For this we need toredirect to register page if there
            print('from not valid')
            # print(form.data)
            messages.warning(self.request, 'Form not valid')
        return redirect('/')


class UserSignIn(View):
    def get(self, request, *args, **kwargs):
        messages.info(self.request, 'Try to login first, then make your booking easy')
        return redirect('/')

    def post(self, request, *args, **kwargs):
        if self.request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')

            user_auth = authenticate(email=email, password=password)

            if user_auth:
                # we need to check if the auth_user is activate to our system
                if user_auth.is_active:
                    # if not request.POST.get('remember_me', None):
                    # make the session to end in one mouth
                    login(request, user_auth)
                    messages.info(self.request, 'welcome home ')
                    return redirect('/')

                else:
                    messages.info(self.request, 'Your account was inactive.Try to activate your account now')
                    return redirect('sign_in')
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(email, password))
                messages.warning(self.request, 'Invalid login details given,')
                return redirect("/")


def user_sign_out(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    messages.warning(request, 'Your signed Out, try to Login again')
    return redirect('/')
