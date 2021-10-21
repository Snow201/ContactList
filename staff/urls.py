from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('person', views.PersonView)

urlpatterns = [
    path('',include(router.urls)),
    path('person/',views.alljson,name='json'),
    path('person/<int:person_id>/',views.jsondata,name='jsondata'),
    path('info/<int:person_id>/',views.person,name='info'),
    path('info/all/',views.allhtml,name='html'),
]
