from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('person', views.PersonView)
urlpatterns = [
    path('',include(router.urls)),
    path('person/<int:person_id>/',views.jsondata,name='jsondata'),
]
