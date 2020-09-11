from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.conf import settings


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


class Friends(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    friends = models.ManyToManyField("Friends", blank=True)

    def __str__(self):
        return str(self.user.username)


class FriendRequest(models.Model):
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
