"""lab_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from WineShop.views import WineViewSet, CategoryViewSet, CustomerViewSet, ManufacturerViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router_1 = routers.DefaultRouter()
router_2 = routers.DefaultRouter()
router_3 = routers.DefaultRouter()
router_4 = routers.DefaultRouter()

router_1.register(r'wines', WineViewSet)
router_2.register(r'customers', CustomerViewSet)
router_3.register(r'categories', CategoryViewSet)
router_4.register(r'manufacturers', ManufacturerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path('wines/', include((router_1.urls))),
    path('customers/', include((router_2.urls))),
    path('categories/', include((router_3.urls))),
    path('manufacturers/', include((router_4.urls)))

]