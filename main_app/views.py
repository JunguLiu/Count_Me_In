from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plans


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
