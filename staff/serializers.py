from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name','last_name','email','phone','hired_at','salary','job','department','is_manager']