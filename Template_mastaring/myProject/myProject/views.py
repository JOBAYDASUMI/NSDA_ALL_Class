from django.shortcuts import render,redirect
from django.http import HttpResponse



def addTaskPage(req):
    return render(req, "addTaskPage.html")

def basePage(req):
    return render(req,'basePage.html')