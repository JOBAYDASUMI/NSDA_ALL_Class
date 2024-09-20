from django.shortcuts import render, redirect


def basePage(req):
    return render(req, 'basePage.html')

def index(req):
    return render (req, 'index.html')

def login(req):
    return render (req, 'login.html')

def register(req):
    return render (req, 'register.html')