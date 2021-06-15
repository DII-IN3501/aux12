from django.urls import path
from mainApp.views import index

urlpatterns = [
    path('', index, name="index"),
]
