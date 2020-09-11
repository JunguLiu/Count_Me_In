from .models import Plans, FriendRequest, Friends
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plans, Workouts, Wishlist, Photo, FriendRequest, Friends

from django.views.decorators.csrf import csrf_exempt

import uuid
import boto3

S3_BASE_URL = "https://s3.us-east-1.amazonaws.com/"
BUCKET = 'countmeincmi'
# plans


class PlansCreate(CreateView):
    model = Plans
    fields = ["name", "workout", "url"]


class PlansUpdate(UpdateView):
    model = Plans
    fields = ["name", "workout"]


class PlansDelete(DeleteView):
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
    if Wishlist.objects.get(user_id=request.user.id) == False:
        wishlist = Wishlist(user_id=request.user.id)
        wishlist.save()
    else:
        wishlist = Wishlist(user_id=request.user.id)

    all_wishlist = wishlist.workout.all()
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


# def main_page(request):
#     return render(request, "main-page.html")


def assoc_wishlist_to_plan(request, plan_id, workout_id):
    Plans.objects.get(id=plan_id).workout.add(workout_id)
    return redirect('detail', plan_id=plan_id)


def add_photo(request, plan_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
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
    workouts = Workouts.objects.all()
    print("WWWWWWWWWWWWWWWWWW")
    for workout in workouts:
        print(workout.id)
        print(workout.location)
        print(workout.category)

    return render(request, "main-page.html", {"workouts": workouts})


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
    if Wishlist.objects.get(user_id=request.user.id) == False:
        wishlist = Wishlist(user_id=request.user.id)
        wishlist.save()
    else:
        wishlist = Wishlist(user_id=request.user.id)

    print("_____________________")
    return render(request, "workout_detail/workout_detail.html", {"workout": workout, "wishlist": wishlist})

# wishlist


def wishlists_index(request):
    # wishlists = Wishlist.objects.get(id=wishlist_id).workouts_set.all()
    print("*****here******")
    if Wishlist.objects.get(user_id=request.user.id) == False:
        wishlist = Wishlist(user_id=request.user.id)
        wishlist.save()
    else:
        wishlist = Wishlist(user_id=request.user.id)

    wishlists = wishlist.workout.all()
    print(wishlists)
    return render(request, "wishlist/wishlist.html", {"wishlists": wishlists})


def assoc_wishlist(request, workout_id):
    # Note that you can pass a toy's id instead of the whole object
    # Workouts.objects.get(id=workout_id).wishlists.add(wishlist_id)
    print("++++++++++assoc_wishlist++++++++++")
    wishlist = Wishlist(user_id=request.user.id)
    wishlist.save()
    wishlist.workout.add(workout_id)
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
    if Friends.objects.filter(user1=request.user).count():
        friends = Friends.objects.get(user1=request.user)
    else:
        friends = None

    if FriendRequest.objects.filter(to_user=request.user).count():
        friends_request = FriendRequest.objects.get(to_user=request.user)
    else:
        friends_request = None

    return render(request, "friends/friends.html", {"friends": friends, "friends_request": friends_request, "error": False})


@csrf_exempt
def addFriends(request):
    User = get_user_model()

    if str(request.user) == str(request.POST.get('to_user')) or User.objects.filter(
            username=request.POST.get('to_user')).count() == 0 or FriendRequest.objects.filter(from_user=request.user,
                                                                                               to_user=request.POST.get('to_user')).count() != 0:
        if Friends.objects.filter(user1=request.user).count():
            friends = Friends.objects.get(user1=request.user)
        else:
            friends = None

        if FriendRequest.objects.filter(to_user=request.user).count():
            friends_request = FriendRequest.objects.get(to_user=request.user)
        else:
            friends_request = None
        return render(request, "friends/friends.html", {"friends": friends, "friends_request": friends_request, "error": True})
    else:
        r = FriendRequest(from_user=request.user,
                          to_user=request.POST.get('to_user'))
        r.save()

        return redirect('/friends')


def acceptRequest(request, id):
    r = FriendRequest.objects.get(id=id)
    f = Friends(user1=r.from_user, user2=r.to_user)
    f.save()
    FriendRequest.objects.filter(id=id).delete()
    return redirect('/friends')


def declineRequest(request, id):
    FriendRequest.objects.filter(id=id).delete()
    return redirect('/friends')
