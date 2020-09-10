from django.urls import path
from . import views
from django.conf.urls import url, include
urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('plans/', views.plans_index, name='index'),
    path('plans/<int:plan_id>/', views.plans_detail, name='detail'),
    path('plans/create/', views.PlanCreate.as_view(), name='plans_create'),
    path('plans/<int:pk>/update/', views.PlanUpdate.as_view(), name='plans_update'),
    path('plans/<int:pk>/delete/', views.PlanDelete.as_view(), name='plans_delete'),
    path('plans/<int:plan_id>/assoc_wishlist/<int:wishlist_id>/',
         views.assoc_wishlist, name='assoc_wishlist_to_plan'),
    # path('plans/<int:plan_id>/add_photo/', views.add_photo, name='add_photo'),
    # detail
    path('workouts/<int:workout_id>/',
         views.workouts_detail, name='workout_detail'),
    # wishlist
    path('wishlists/<int:wishlist_id>',
         views.wishlists_index, name='wishlists_index'),
    path('wishlists/<int:workout_id>/assoc_wishlist/<int:wishlist_id>/',
         views.assoc_wishlist, name='assoc_wishlist'),
    path('wishlists/<int:workout_id>/plans',
         views.wishlist_to_plan, name="wishlist_to_plan"),
    path('wishlists/<int:workout_id>/plans/<int:plan_id>/',
         views.add_to_plan, name="add_to_plan"),


    # login...
    path('accounts/signup/', views.signup, name='signup'),

]
