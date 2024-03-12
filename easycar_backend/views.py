from rest_framework import generics, status
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
import json
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Car
from .serializers import CarSerializer


class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


@api_view(['POST'])
@parser_classes((MultiPartParser, FormParser))
@permission_classes([IsAuthenticated])  # Ensure that the user is authenticated
def car_create_view(request, format=None):
    print("Car create view entered")
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        owner = request.user
        print("serializer is valid")
        print("Owner is:" + str(owner))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        try:
            car = self.get_object()
            serializer = self.get_serializer(car)
            return Response(serializer.data)
        except Car.DoesNotExist:
            raise NotFound('A car with this ID does not exist.')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Check if all fields are provided
        if not all(key in data for key in ['username', 'email', 'password', 'first_name', 'last_name']):
            return JsonResponse({'error': 'All fields are required.'}, status=400)

        # Use create_user instead of create to handle password hashing
        user = User.objects.create_user(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password']
        )
        login(request, user)  # Log the user in
        return JsonResponse({'id': user.id, 'username': user.username}, status=201)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            print("The user logged in, ID: " + str(user.id) + ". Token = " + str(refresh))
            return JsonResponse({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'id': user.id,
                'username': user.username
            }, status=200)
        return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': 'Logged out'}, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
