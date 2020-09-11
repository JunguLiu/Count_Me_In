from django.db import models
from django.urls import reverse

from django.conf import settings
# from datetime import date

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

    url = models.ImageField("image", upload_to='plan_image', blank=True)
    wishlists = models.ManyToManyField("Wishlist")
    workout = models.ManyToManyField(Workouts)


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


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     weight = models.IntegerField()
#     goalWeight = models.IntegerField()
#     age = models.IntegerField()
#     plans = models.ForeignKey(Plans, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name



class Wishlist(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    workout = models.ManyToManyField(Workouts)

    # def __str__(self):
    #     return f"{self.user}'s wishlist"


    def __str__(self):
        return str(self.user.username)



class Friends(models.Model):
    user1 = models.CharField(max_length=150)
    user2 = models.CharField(max_length=150)


class FriendRequest(models.Model):
    to_user = models.CharField(max_length=150)
    from_user = models.CharField(max_length=150)

