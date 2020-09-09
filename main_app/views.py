from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plans, Workouts


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
    return render(request, "plan/detail.html", {"plan": plan})


def plans_create(request):
    return render(request, "plan/create.html")


def main_page(request):
    return render(request, "main-page.html")


def workouts_detail(request, workout_id):
    workout = Workouts.objects.get(id=workout_id)
    return render(request, "workout_detail/workout_detail.html", {"workout": workout})

def wishlists_index(request):
    return render(request, "wishlist.html")
