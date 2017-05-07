from __future__ import unicode_literals

from django.db import models
class members(models.Model):
    car_owner_name=models.CharField(max_length=50)
    age=models.IntegerField(default=0)
    address=models.CharField(max_length=100)
    mobile_number=models.IntegerField(default=0)
    car_name=models.CharField(max_length=15)
    car_number=models.CharField(max_length=10)
    def __str__(self):
        return self.car_number
    
    