
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/',homePage, name="homePage"),
    path('headerPage/',headerPage, name="headerPage"),
    path('dashbord/',dashbord, name="dashbord"),
    path('loginPage/',loginPage, name="loginPage"),
    path('registerPage/',registerPage, name="registerPage"),
    path('footerPage/',footerPage, name="footerPage"),
    path('add_Event/',add_Event, name="add_Event"),
    path('edit_Event/',edit_Event, name="edit_Event"),
    path('view_Event/',view_Event, name="view_Event"),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
