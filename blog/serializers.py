from rest_framework import serializers
from .models import *


class AboutUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs.objects.all()
        fields = '__all__'


class SchedulesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Schedules.objects.all()
        fields = '__all__'


class ClassesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classes.objects.all()
        fields = '__all__'



class ContactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contacts.objects.all()
        fields = '__all__'


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users.objects.all()
        fields = '__all__'

