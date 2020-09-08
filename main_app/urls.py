from django.urls import path
from . import views

urlpatterns = [
    path('/plan', views.plans_index, name='index'),

    path('', views.main_page, name='index'),
]
