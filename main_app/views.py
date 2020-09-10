from .models import Plans
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plans, Workouts, Wishlist
import uuid
import boto3

S3_BASE_URL = "https://s3.us-east-1.amazonaws.com/"
BUCKET = 'countmeincmi'
# plans


class PlanCreate(CreateView):
    model = Plans
    fields = "__all__"


class PlanUpdate(UpdateView):
    model = Plans
    fields = "__all__"


class PlanDelete(DeleteView):
    model = Plans
    success_url = '/plans/'


def plans_index(request):
    plans = Plans.objects.all()
    return render(request, "plan/index.html", {"plans": plans})


def plans_detail(request, plan_id):
    plan = Plans.objects.get(id=plan_id)
    print("***********")
    print(plan)
    workouts_not_in_plan = Wishlist.objects.exclude(
        id__in=plan.wishlists.all().values_list('id'))
    print("*****HERE******")
    return render(request, "plan/detail.html", {"plan": plan, "wishlists": workouts_not_in_plan})


def plans_create(request):
    return render(request, "plan/create.html")


def main_page(request):
    return render(request, "main-page.html")


def assoc_wishlist_to_plan(request, plan_id, wishlist_id):
    Plans.objects.get(id=plan_id).wishlist.add(wishlist_id)
    return redirect('detail', plan_id=plan_id)


def show_main(request):
    return render(request, "main-page.html")


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# workouts


def workouts_detail(request, workout_id):
    workout = Workouts.objects.get(id=workout_id)
    wishlist = Wishlist.objects.all()
    print("_____________________")
    return render(request, "workout_detail/workout_detail.html", {"workout": workout, "wishlist": wishlist})

# wishlist


def wishlists_index(request, wishlist_id):
    wishlists = Wishlist.objects.get(id=wishlist_id).workouts_set.all()
    return render(request, "wishlist/wishlist.html", {"wishlists": wishlists})


def assoc_wishlist(request, workout_id, wishlist_id):
    # Note that you can pass a toy's id instead of the whole object
    Workouts.objects.get(id=workout_id).wishlists.add(wishlist_id)
    return redirect('wishlists_index', wishlist_id=wishlist_id)


def wishlist_to_plan(request, workout_id):
    print("*****HERE222******")
    print(workout_id)

    plans = Plans.objects.all()
    return render(request, "plan/new_workout.html", {"plans": plans, "workout_id": workout_id})


def add_to_plan(request, workout_id, plan_id):
    print("*****HERE222******")
    print(plan_id)
    print(workout_id)
    Plans.objects.get(id=plan_id).wishlists.add(workout_id)
    return redirect('detail', plan_id=plan_id)
