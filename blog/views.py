from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *



class AboutUsViewSet(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializers


class ClassesViewSet(ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializers


class SchedulesViewSet(ModelViewSet):
    queryset = Schedules.objects.all()
    serializer_class = SchedulesSerializers


class ContactsViewSet(ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializers


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers
