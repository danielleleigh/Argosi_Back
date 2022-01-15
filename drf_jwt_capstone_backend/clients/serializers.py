from rest_framework import serializers
from .models import  Appointment, Client
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
User = get_user_model()

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['user', 'first_name', 'last_name', 'username','password','dob', 'birth_time', 'email', 'birth_zip']


class ClientRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[
                                   UniqueValidator(queryset=Client.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Client
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ['user', 'first_name', 'last_name', 'username','password','dob', 'birth_time', 'email', 'birth_zip']


    def create(self, validated_data):

        client = Client.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            password=validated_data['password'],
            dob=validated_data['dob'],
            birth_time=validated_data['birth_time'],
            email=validated_data['email'],
            birth_zip=validated_data['birth_zip'],
            # If added new columns through the User model, add them in this
            # create method call in the format as seen above
        )
        client.set_password(validated_data['password'])
        client.save()

        return  client
    
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['client','date', 'time', 'notes']