from django.urls import path
from . import views

urlpatterns = [
    path('', views.basic_calculator, name='basic_calculator'),
]
