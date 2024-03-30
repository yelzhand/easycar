from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import CarListCreateView, CarDetailsView, PaymentView
from .views import get_user_info, change_password, list_bookings
urlpatterns = [
    # path('cars/create-booking/', views.create_booking, name='create-booking'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('car-create/', views.car_create_view, name='car-create'),
    path('cars/<int:id>/', CarDetailsView.as_view(), name='car-detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('become_host/',)
    path('bookings/', list_bookings, name='list_bookings'),
     path('upload_license/', views.upload_license, name='upload_license'),
    path('api/userinfo/', get_user_info, name='get_user_info'),
    path('api/change-password/', change_password, name='change_password'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
