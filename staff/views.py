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
    return redirect('staff/person')

def person(request, person_id):
    person = Person.objects.get(id=person_id)
    context = {'person':person}
    return render(request,'cv.html',context)


def alljson(request):
    return redirect('staff/person')

def allhtml(request):
    workers = Person.objects.all()
    context = {'workers':workers}
    return render(request,'cv.html',context)