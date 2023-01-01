from django.db import models

# Create your models here.


class Employee(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.firstname