from django.shortcuts import render,redirect
from django.http import HttpResponse


def index(req):
    return render(req, 'index.html')

def registerPage(req):
    return render(req, 'registerPage.html')

def loginPage(req):
    return render(req, 'loginPage.html')