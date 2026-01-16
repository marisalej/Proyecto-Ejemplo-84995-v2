from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import *


urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile_detail, name="perfil_detail"),
    path("profile/change", profile_change, name="profile_edit"),
]