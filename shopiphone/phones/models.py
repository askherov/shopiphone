from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=16)
    lastname = models.CharField(max_length=32)
    def __str__(self) ->str:
        return f"{self.firstname} {self.lastname} {self.pk}"
    

class Phone(models.Model):
    model = models.CharField(max_length=10)
    rom = models.SmallIntegerField()
    ram = models.SmallIntegerField()
    color = models.CharField(max_length=7)
    is_new = models.BooleanField()
    weight = models.FloatField()
    dimension = models.FloatField()
    battery_capacity = models.SmallIntegerField()
    operating_system = models.CharField(max_length=10)
    def __str__(self) ->str:
        return f"{self.model} {self.pk}"
    
class Car(models.Model):
    model = models.CharField(max_length=3)
    color = models.CharField(max_length=10)
    engine = models.FloatField()
    seats = models.SmallIntegerField()
    production_year = models.DateTimeField()
    is_new = models.BooleanField()
    painted_part = models.CharField(max_length=10)
    oil_sort = models.CharField(max_length=7)
    car_type = models.CharField(max_length=12)

    def __str__(self) -> str:
        return f"{models}"