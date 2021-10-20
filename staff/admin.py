from django.contrib import admin
from .models import Person,Department,Job,Manager
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id','name','last_name','phone','salary','hired_at')

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('manager',)

admin.site.register(Person,PersonAdmin)
admin.site.register(Department)
admin.site.register(Job)
admin.site.register(Manager,ManagerAdmin)