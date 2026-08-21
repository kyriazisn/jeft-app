from django.contrib import admin
from django.urls import path

from apps.accounts.views import signin, signup, signout
from apps.requests.views import create_request, my_request, request_list, request_submitted

urlpatterns = [
    path("", request_list, name="home"),
    path("accounts/signup/", signup, name="signup"),
    path("accounts/login/", signin, name="login"),
    path("accounts/logout/", signout, name="logout"),
    path("requests/create/", create_request, name="create_request"),
    path("requests/submitted/", request_submitted, name="request_submitted"),
    path("requests/mine/", my_request, name="my_request"),
    path("admin/", admin.site.urls),
]
