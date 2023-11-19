from .views import CarListCreateView, CarRetrieveUpdateDestroyView
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('cars/create/', CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<int:id>/', CarRetrieveUpdateDestroyView.as_view(), name='car-retrieve-update-destroy')
]
