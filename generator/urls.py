from django.urls import path
from .views import *
urlpatterns = [
    path("", hello),
    path("password/", password, name = "password"),
]
