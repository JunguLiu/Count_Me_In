from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.


class Workouts(models.Model):
    name = models.CharField(max_length=100),


class Comments(models.Model):
    name = models.CharField(max_length=100),


class Plans(models.Model):
    name = models.CharField(max_length=100),
    workouts = models.ManyToManyField(Workouts),
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE),
    date = models.DateField

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plan_id': self.id})
