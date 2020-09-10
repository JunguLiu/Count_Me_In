from django.db import models
from django.urls import reverse
from django.conf import settings
# from datetime import date
from django.contrib.auth.models import User


class Workouts(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    category = models.CharField(max_length=100)
    image = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Plans(models.Model):
    name = models.CharField(max_length=100)
    url = models.ImageField("image", upload_to='plan_image', blank=True)
    wishlists = models.ManyToManyField("Wishlist")
    workout = models.ManyToManyField(Workouts)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plan_id': self.id})


class Comments(models.Model):
    name = models.CharField(max_length=100)
    plans = models.ForeignKey(Plans, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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


class Photo(models.Model):
    url = models.CharField(max_length=200)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cat_id: {self.plan_id} @{self.url}"


class Friends(models.Model):
    user1 = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='user2', on_delete=models.CASCADE)


class FriendRequest(models.Model):
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
