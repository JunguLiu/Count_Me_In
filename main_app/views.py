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
    wishlist = Wishlist.objects.filter(plans=plan_id)
    wishlist_all = Wishlist.objects.all()
    workouts_not_in_plan = Wishlist.objects.exclude(
        id__in=wishlist.values_list('id'))

    # wishlists_plan_doesnt_have = Wishlist.objects.exclude(
    # id__in = plan.wishlist.all().values_list('id'))
    return render(request, "plan/detail.html", {"plan": plan, "wishlist": wishlist, "wishlists": workouts_not_in_plan})


def plans_create(request):
    return render(request, "plan/create.html")


def main_page(request):
    return render(request, "main-page.html")


def assoc_wishlist(request, plan_id, wishlist_id):
    Plans.objects.get(id=plan_id).wishlist.add(wishlist_id)
    return redirect('detail', plan_id=plan_id)


# workouts
def workouts_detail(request, workout_id):
    workout = Workouts.objects.get(id=workout_id)
    return render(request, "workout_detail/workout_detail.html", {"workout": workout})


def wishlists_index(request):
    return render(request, "wishlist.html")


def show_main(request):
    return render(request, "main-page.html")
