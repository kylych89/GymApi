from rest_framework import serializers
from .models import *


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs.objects.all()
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User.objects.all()
        fields = '__all__'


class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules.objects.all()
        fields = '__all__'


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes.objects.all()
        fields = '__all__'



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact.objects.all()
        fields = '__all__'

