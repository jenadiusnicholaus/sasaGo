from django.urls import path
from . import views

urlpatterns = [
    path("register", views.UserSignUp.as_view(), name="register"),
    path("login", views.UserSignIn.as_view(), name="login"),

    path('logout',views.user_sign_out, name = 'logout')
]
