from django.db import models

# Create your models here.

class Booking(models.Model):
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveIntegerField()

class Table(models.Model):
    date = models.DateField()
    time = models.TimeField()
    table_number = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)