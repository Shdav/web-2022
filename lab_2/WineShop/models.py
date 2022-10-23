from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=10000)
    description = models.CharField(max_length=10000)

    class Meta:
        managed = True
        db_table = 'manufacturers'


class Wine(models.Model):
    name = models.CharField(max_length=10000)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    words = models.CharField(max_length=10000)

    class Meta:
        managed = True
        db_table = 'wines'


class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    favourites = models.ManyToManyField(Wine)

    class Meta:
        managed = True
        db_table = 'users'