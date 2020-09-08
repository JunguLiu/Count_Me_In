from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans_index, name='index'),
]
