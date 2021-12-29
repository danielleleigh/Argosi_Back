from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateTimeField(max_length=50)
    email = models.EmailField(max_length=50)
    birth_zip = models.IntegerField()