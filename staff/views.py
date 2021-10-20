from django.shortcuts import render,redirect
from rest_framework import viewsets,permissions
from .models import Person
from .serializers import PersonSerializer


# Create your views here.

class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


def jsondata(request):

    return redirect('staffperson')


