
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index, name='index'),
    path('registerPage/',registerPage,name='registerPage'),
    path('loginPage/',loginPage, name='loginPage'),
    
]
