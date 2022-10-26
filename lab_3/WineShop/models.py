from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=10000)

    class Meta:
        managed = True
        db_table = 'manufacturers'


class Category(models.Model):
    name = models.CharField(max_length=10000)

    class Meta:
        managed = True
        db_table = 'category'


class Wine(models.Model):
    name = models.CharField(max_length=10000)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=10000)
    prise = models.FloatField()

    class Meta:
        managed = True
        db_table = 'wines'


class Customer(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    favourites = models.ManyToManyField(Wine)

    class Meta:
        managed = True
        db_table = 'customers'
