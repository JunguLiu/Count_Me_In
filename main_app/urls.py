from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.plans_index, name='index'),
    path('plans/<int:plan_id>/', views.plans_detail, name='detail'),
    path('plans/newPlans/', views.plans_create, name='create'),


]
