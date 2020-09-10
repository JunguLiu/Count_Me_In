from .models import Plans
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plans, Workouts, Wishlist, Photo, FriendRequest, Friends

import uuid
import boto3

S3_BASE_URL = "https://s3.us-east-1.amazonaws.com/"
BUCKET = 'countmeincmi'
# plans


class PlanCreate(CreateView):
    model = Plans
    fields = ["name", "workout", "url"]


class PlanUpdate(UpdateView):
    model = Plans
    fields = ["name", "workout"]


class PlanDelete(DeleteView):
    model = Plans
    success_url = '/plans/'


def plans_index(request):
    plans = Plans.objects.all()
    return render(request, "plan/index.html", {"plans": plans})


def plans_detail(request, plan_id,):
    plan = Plans.objects.get(id=plan_id)
    workouts = plan.workout.all()
    print("***********")
    print(request.user.id)
    print(plan.workout)
    print(plan.workout.all())
    all_wishlist = Wishlist.objects.get(user_id=request.user.id).workout.all()
    print("++++++++++")
    print(all_wishlist)
    workouts_not_in_plan = all_wishlist.exclude(
        id__in=plan.workout.all().values_list('id'))
    print("*****HERE******")
    print(workouts_not_in_plan)
    print(plan.workout.all())

    return render(request, "plan/detail.html", {"plan": plan, "wishlists": workouts_not_in_plan, "workouts": workouts})


def plans_create(request):
    return render(request, "plan/create.html")


def main_page(request):
    return render(request, "main-page.html")


def assoc_wishlist_to_plan(request, plan_id, workout_id):
    Plans.objects.get(id=plan_id).workout.add(workout_id)
    return redirect('detail', plan_id=plan_id)


def add_photo(request, plan_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        print("here***************")
        print(photo_file)
        print(plan_id)

        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6]+photo_file.name[photo_file.name.rfind('.'):]
        try:
            print("here***************")
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, plan_id=plan_id)
            photo.save()
            print(photo)

        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', plan_id=plan_id)


def unassoc_workout(request, plan_id, workout_id):
    Plans.objects.get(id=plan_id).workout.remove(workout_id)
    return redirect('detail', plan_id=plan_id)

# main page


def show_main(request):
    return render(request, "main-page.html")


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# workouts


def workouts_detail(request, workout_id):
    workout = Workouts.objects.get(id=workout_id)
    wishlist = Wishlist.objects.all()
    print("_____________________")
    return render(request, "workout_detail/workout_detail.html", {"workout": workout, "wishlist": wishlist})

# wishlist


def wishlists_index(request):
    # wishlists = Wishlist.objects.get(id=wishlist_id).workouts_set.all()
    print("*****here******")
    wishlists = Wishlist.objects.get(user_id=request.user.id).workout.all()
    print(wishlists)
    return render(request, "wishlist/wishlist.html", {"wishlists": wishlists})


def assoc_wishlist(request, workout_id):
    # Note that you can pass a toy's id instead of the whole object
    # Workouts.objects.get(id=workout_id).wishlists.add(wishlist_id)
    print("++++++++++assoc_wishlist++++++++++")
    Wishlist.objects.get(user_id=request.user.id).workout.add(workout_id)
    return redirect('wishlists_index')


def wishlist_to_plan(request, workout_id):
    print("*****HERE222******")
    plans = Plans.objects.all()
    return render(request, "plan/new_workout.html", {"plans": plans, "workout_id": workout_id})


def add_to_plan(request, workout_id, plan_id):
    print("*****HERE3333******")
    print(plan_id)
    print(workout_id)
    plan1 = Plans.objects.get(id=plan_id)
    workout = Workouts.objects.get(id=workout_id)
    plan1.workout.add(workout_id)
    plan2 = plan1.workout.all()
    # Cat.objects.get(id=cat_id).toys.add(toy_id)
    print(f"plan 1 is ${plan1}")
    print(f"plan2  is ${plan2}")
    print(f"workout  is ${workout}")

    return redirect('detail', plan_id=plan_id)


def friends(request):
    print(request.user.id)
    friends = Friends.objects.get(user1=request.user.id)
    friends_request = FriendRequest.objects.get(to_user_id=request.user.id)
    return render(request, "friends/friends.html", {"friends": friends, "friends_request": friends_request})
