from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.plans_index, name='index'),
    path('plans/<int:plan_id>/', views.plans_detail, name='detail'),
    path('plans/newPlans/', views.plans_create, name='create'),

    # detail
    path('workouts/<int:workout_id>/',
         views.workouts_detail, name='workout_detail'),
    # wishlist
    path('wishlists/', views.wishlists_index, name='wishlists_index'),

]
