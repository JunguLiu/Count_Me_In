from django.urls import path
from . import views
from django.conf.urls import url, include
urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('plans/', views.plans_index, name='index'),
    path('plans/<int:plan_id>/', views.plans_detail, name='detail'),
    path('plans/create/', views.PlansCreate.as_view(), name='plans_create'),
    path('plans/<int:pk>/update/', views.PlansUpdate.as_view(), name='plans_update'),
    path('plans/<int:pk>/delete/', views.PlansDelete.as_view(), name='plans_delete'),
    path('plans/<int:plan_id>/assoc_wishlist_to_plan/<int:workout_id>/',
         views.assoc_wishlist_to_plan, name='assoc_wishlist_to_plan'),
    path('plans/<int:plan_id>/add_photo/', views.add_photo, name='add_photo'),
    path('plans/<int:plan_id>/unassoc_toy/<int:workout_id>/',
         views.unassoc_workout, name='unassoc_workout'),

    # path('plans/<int:plan_id>/add_photo/', views.add_photo, name='add_photo'),
    # detail
    path('workouts/<int:workout_id>/',
         views.workouts_detail, name='workouts_detail'),
    # wishlist
    path('wishlists',
         views.wishlists_index, name='wishlists_index'),
    path('wishlists/<int:workout_id>/assoc_wishlist/',
         views.assoc_wishlist, name='assoc_wishlist'),
    path('wishlists/<int:workout_id>/plans/',
         views.wishlist_to_plan, name="wishlist_to_plan"),
    path('wishlists/<int:workout_id>/plans/<int:plan_id>/',
         views.add_to_plan, name="add_to_plan"),


    # login...
    path('accounts/signup/', views.signup, name='signup'),


    # friends

    path('friends/', views.friends, name='friends'),
    path('friends/add', views.addFriends, name='addFriends'),
    path('friends/acceptRequest/<int:id>/',
         views.acceptRequest, name='acceptRequest'),
    path('friends/declineRequest/<int:id>/',
         views.declineRequest, name='acceptRequest')

]
