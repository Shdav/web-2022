from rest_framework import viewsets
from WineShop.serializers import WineSerializer, CategorySerializer, CustomerSerializer, ManufacturerSerializer
from WineShop.models import Wine, Category, Customer, Manufacturer


class WineViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Wine.objects.all()
    serializer_class = WineSerializer  # Сериализатор для модели


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Category.objects.all()
    serializer_class = CategorySerializer  # Сериализатор для модели


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer  # Сериализатор для модели


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer  # Сериализатор для модели
