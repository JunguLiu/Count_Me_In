from django.db import models
from django.urls import reverse


class Comments(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Workouts(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    category = models.CharField(max_length=100)
    image = models.TextField(max_length=100)
    #wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Plans(models.Model):
    name = models.CharField(max_length=100)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)
    # date = models.DateField()
    # image = models.ImageField
    # workouts = models.ManyToManyField(Workouts)

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


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s wishlist"

