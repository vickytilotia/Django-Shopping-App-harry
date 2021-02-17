# This file is custom created

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "BlogHome"),
]
