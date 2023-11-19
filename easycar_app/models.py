from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

