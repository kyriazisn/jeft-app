from django.contrib import admin
from django.urls import path

from apps.accounts.views import signin, signup, signout
from apps.requests.views import request_list

urlpatterns = [
    path("", request_list, name="home"),
    path("accounts/signup/", signup, name="signup"),
    path("accounts/login/", signin, name="login"),
    path("accounts/logout/", signout, name="logout"),
    path("admin/", admin.site.urls),
]
