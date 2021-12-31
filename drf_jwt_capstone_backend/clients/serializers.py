from rest_framework import serializers
from .models import Appointment, Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'dob', 'sun_sign', 'moon_sign', 'rising_sign', 'email', 'birth_zip' ]

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'date_time', 'past_summary']