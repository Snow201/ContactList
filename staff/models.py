from django.db import models

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.BigIntegerField()
    img = models.ImageField(upload_to='photos/products',blank=True)
    hired_at = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    job = models.ForeignKey(Job,on_delete=models.CASCADE,null=True,blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return (self.name+' '+self.last_name)



class Manager(models.Model):
    manager = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    workers = models.ManyToManyField(Person,blank=True,related_name='workers')

    def __unicode__(self):
        return self.manager