from WineShop.models import Wine, Manufacturer, Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Customer
        # Поля, которые мы сериализуем
        fields = ["pk", "login", "password", "favourites"]


class WineSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Wine
        # Поля, которые мы сериализуем
        fields = ["pk", "name", "manufacturer", "category", "description", "prise"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Wine
        # Поля, которые мы сериализуем
        fields = ["pk", "name"]


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Wine
        # Поля, которые мы сериализуем
        fields = ["pk", "name"]