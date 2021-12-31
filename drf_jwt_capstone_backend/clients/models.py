from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    first_name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, default=None)
    dob = models.DateTimeField(max_length=50, default=None)
    sun_sign = models.CharField(max_length=50, default=None)
    moon_sign = models.CharField(max_length=50, default=None)
    rising_sign = models.CharField(max_length=50, default=None)
    email = models.EmailField(max_length=50, default=None)
    birth_zip = models.IntegerField()

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=CASCADE)
    date_time = models.DateTimeField(max_length=100, default=None)
    past_summary = models.TextField(max_length=400, default=None)
    

    