from .views import CarListCreateView, CarRetrieveUpdateDestroyView
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<int:id>/', CarRetrieveUpdateDestroyView.as_view(), name='car-retrieve-update-destroy')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
