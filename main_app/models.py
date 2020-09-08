from django.db import models
from django.urls import reverse
from datetime import date


class Workouts(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    category = models.CharField(max_length=100)
    image = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Comments(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Plans(models.Model):
    name = models.CharField(max_length=100),
    workouts = models.ManyToManyField(Workouts)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)
    date = models.DateField
    image = models.ImageField

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plan_id': self.id})


class User(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    goalWeight = models.IntegerField()
    age = models.IntegerField()
    plans = models.ForeignKey(Plans, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
