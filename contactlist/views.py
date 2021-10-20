from django.shortcuts import render,redirect
from staff.models import Person,Department,Job,Manager

def index(request):
    workers = Person.objects.all().filter()

    context = {'workers':workers,}
    return render(request,'index.html',context)


