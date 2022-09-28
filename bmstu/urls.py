from bmstu_lab import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('', views.GetOrders),
    path('order/<int:id>/', views.GetOrder, name='order_url'),
]