from django.contrib import admin
from django.urls import path

from apps.requests.views import request_list

urlpatterns = [
    path("", request_list, name="home"),
    path("admin/", admin.site.urls),
]
