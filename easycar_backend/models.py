from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Assuming you have a User model (Django's default or a custom one)
User = settings.AUTH_USER_MODEL


class Car(models.Model):
    FUEL_TYPE_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ]
    TRANSMISSION_CHOICES = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    ]
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    ]
    COLOR_CHOICES = [
        ('black', 'Black'),
        ('white', 'White'),
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('gray', 'Gray'),
        ('silver', 'Silver'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
        ('purple', 'Purple'),
    ]

    LOCATION_CHOICES = [
        ('Astana, Kazakhstan', 'Astana, Kazakhstan'),
        ('Almaty, Kazakhstan', 'Almaty, Kazakhstan'),
        ('Shymkent, Kazakhstan', 'Shymkent, Kazakhstan'),
        ('Karaganda, Kazakhstan', 'Karaganda, Kazakhstan'),
        ('Aktobe, Kazakhstan', 'Aktobe, Kazakhstan'),
        ('Taraz, Kazakhstan', 'Taraz, Kazakhstan'),
        ('Pavlodar, Kazakhstan', 'Pavlodar, Kazakhstan'),
        ('Ust-Kamenogorsk, Kazakhstan', 'Ust-Kamenogorsk, Kazakhstan'),
        ('Semey, Kazakhstan', 'Semey, Kazakhstan'),
        ('Atyrau, Kazakhstan', 'Atyrau, Kazakhstan'),
        ('Kostanay, Kazakhstan', 'Kostanay, Kazakhstan'),
        ('Kyzylorda, Kazakhstan', 'Kyzylorda, Kazakhstan'),
        ('Aktau, Kazakhstan', 'Aktau, Kazakhstan'),
        ('Kokshetau, Kazakhstan', 'Kokshetau, Kazakhstan'),
        ('Taldykorgan, Kazakhstan', 'Taldykorgan, Kazakhstan'),
        ('Ekibastuz, Kazakhstan', 'Ekibastuz, Kazakhstan'),
        ('Petropavl, Kazakhstan', 'Petropavl, Kazakhstan'),
        ('Oral, Kazakhstan', 'Oral, Kazakhstan'),
        ('Temirtau, Kazakhstan', 'Temirtau, Kazakhstan'),
        ('Turkestan, Kazakhstan', 'Turkestan, Kazakhstan'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars')
    make = models.CharField(max_length=50, default='Toyota')
    model = models.CharField(max_length=50, default='RAV4')
    year = models.IntegerField(default='2001')
    license_plate = models.CharField(max_length=20, default='222ZNO01')
    vin = models.CharField(max_length=17, verbose_name='VIN', default='123ZKA02LNQLB')
    color = models.CharField(max_length=30, choices=COLOR_CHOICES, default='blue')
    seats = models.IntegerField(default='2')
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, default='Astana,Kazakhstan')
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, default='150')
    availability = models.CharField(max_length=12, choices=AVAILABILITY_CHOICES, default='available')
    description = models.TextField(blank=True, default='nice nice car')
    imgUrl = ProcessedImageField(
        upload_to='car_images',
        processors=[ResizeToFill(300, 200)],
        format='JPEG',
        options={'quality': 90}
    )
    active = models.BooleanField(default=True)
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPE_CHOICES, default='automatic')
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES, default='automatic')
    mileage = models.IntegerField(default='2000')

    def __str__(self):
        return f'{self.make} {self.model} - {self.year}'


class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='bookings')
    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, blank=True, null=True)  # Optionally calculated in save method
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    booking_location = models.CharField(max_length=255, blank=True, null=True)  # Optional, use if booking location varies

    def save(self, *args, **kwargs):
        # Calculate total price based on the car's price per day and the number of booking days
        booking_duration = (self.end_datetime - self.start_datetime).days + 1  # +1 to include both start and end dates in the booking duration
        # If you charge for partial days, this will need to be more complex
        self.total_price = booking_duration * self.car.price_per_day
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f'Booking {self.id} by {self.user}'