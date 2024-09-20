
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basePage/', basePage, name='basePage'),
    path('addTaskPage/',addTaskPage, name='addTaskPage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
