
from django.contrib import admin
# from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.conf import settings
# from django.viwes.static import serve
# from main_app.views import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
