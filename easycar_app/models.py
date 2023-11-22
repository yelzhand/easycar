from django.db import models


class Car(models.Model):
    id = models.IntegerField(primary_key=True, default="0")
    brand = models.CharField(max_length=100, default="Desc")
    rating = models.IntegerField(default="100")
    carName = models.CharField(max_length=100, default="Desc")
    year = models.IntegerField(default="2001")
    imgUrl = models.ImageField(upload_to='car_images', height_field=None, width_field=None, max_length=100)
    model = models.CharField(max_length=100, default="Desc")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    speed = models.IntegerField(default="70")
    gps = models.CharField(max_length=100, default="gps 2.0")
    transmission = models.CharField(max_length=100, default="Desc")
    description = models.CharField(max_length=200, default="Desc")

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"
