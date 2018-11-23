from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tables', views.tables, name='tables'),
    path('order', views.order, name='order'),
    path('menu', views.order, name='menu'),
]

