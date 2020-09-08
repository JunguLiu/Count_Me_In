from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


def plans_index(request):
    return render(request, "plan/index.html")


def main_page(request):
    return render(request, "main-page.html")
