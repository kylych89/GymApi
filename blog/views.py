from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated



class AboutUsViewSet(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class ClassesViewSet(ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer


class SchedulesViewSet(ModelViewSet):
    queryset = Schedules.objects.all()
    serializer_class = SchedulesSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
