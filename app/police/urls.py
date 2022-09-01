from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/appeals/', include("api.urls")),
]