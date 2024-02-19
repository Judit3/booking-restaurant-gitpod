from django.db import models
from django.contrib.auth.models import User

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

class Restaurant(models.Model):
    total_tables = models.PositiveIntegerField(default=10)  # Example: 10 tables in total