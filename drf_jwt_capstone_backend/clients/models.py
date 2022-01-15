from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.db.models.fields.related import ForeignKey

User = get_user_model()

# Create your models here.
  
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(max_length=50)
    email = models.EmailField(max_length=50)
    birth_zip = models.IntegerField()
    birth_time = models.TimeField(max_length=50,null=True)
    
class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=CASCADE)
    date = models.DateField(max_length=50)
    time = models.TimeField(max_length=50)
    notes = models.TextField(max_length=500, null=True)
  

