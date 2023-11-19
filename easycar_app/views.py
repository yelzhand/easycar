from django.shortcuts import render
from rest_framework import generics

from .models import Car
from .serializers import CarSerializer


class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def post(self, request, *args, **kwargs):
        print("POST request data:", request.data)
        return super().post(request, *args, **kwargs)


class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
