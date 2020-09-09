from django.contrib import admin
from .models import Plans, User, Comments, Workouts

admin.site.register(Plans)
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(Workouts)

admin.site.register(Wishlist)

