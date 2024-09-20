from django.shortcuts import render, redirect
from django.http import HttpResponse

from myApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout





def homePage(req):

    return render(req, 'common/master.html')

def loginPage(req):

    if req.method=='POST':
        user_Name=req.POST.get('username')
        pass_word=req.POST.get('password')

        user=authenticate(
            username=user_Name,password=pass_word
        )
        if user:
            login(req,user)
            return redirect("homePage")
        else:
            return HttpResponse("Invalide Input")
    return render(req, 'common/loginPage.html')

def registerPage(req):

    if req.method=='POST':
        userName=req.POST.get('username')
        userEmail=req.POST.get('email')
        password=req.POST.get('password')
        confirmPassword=req.POST.get('confirmpassword')
        if password==confirmPassword:
            user=User.objects.create_user(
                username=userName,
                email=userEmail,
                password=confirmPassword,
                
            )
            return redirect("loginPage")
        else:
            return HttpResponse("Invalid Password")
    return render(req, 'common/registerPage.html')

def dashbord(req):

    return render(req, 'includes/index.html')

def headerPage(req):

    return render(req, 'includes/headerPage.html')

def footerPage(req):

    return render(req, 'includes/footerPage.html')



def add_Event(req):
    
    if req.method=='POST':
        First_name=req.POST.get('fname')
        Last_name=req.POST.get('lname')
        Student_id=req.POST.get('stuid')
        Gender=req.POST.get('gender')
        DOB=req.POST.get('dob')
        Class=req.POST.get('class')
        Religion=req.POST.get('religion')
        Join_date=req.POST.get('joindate')
        Mobile_number=req.POST.get('mnumber')
        Addmission_number=req.POST.get('addnumber')
        Section=req.POST.get('section')
        Image=req.FILES.get('image')
        Father_name=req.POST.get('fname')
        Father_occupation=req.POST.get('faccupation')
        Father_mobile=req.POST.get('fmobile')
        Father_email=req.POST.get('femail')
        Mother_name=req.POST.get('mname')
        Mother_occution=req.POST.get('moccupation')
        Mother_mobile=req.POST.get('mmobile')
        Mother_email=req.POST.get('memail')
        Present_address=req.POST.get('presentaddress')
        Permanant_address=req.POST.get('permanantaddress')
        
        event=eventModel(
            first_name=First_name,
            last_name=Last_name,
            event_id=Student_id,
            gender=Gender,
            dob=DOB,
            Class=Class,
            religon=Religion,
            joining_date=Join_date,
            mobile_number=Mobile_number,
            addmission_number=Addmission_number,
            section=Section,
            student_img=Image,
            father_name=Father_name,
            father_occupation=Father_occupation,
            father_number=Father_mobile,
            father_email=Father_email,
            mother_name=Mother_name,
            mother_occuoation=Mother_occution,
            mother_number=Mother_mobile,
            mother_email=Mother_email,
            present_address=Present_address,
            permanent_address=Permanant_address,   
        )
        event.save()
        return redirect("view_Event")
        

    return render(req, 'myAdmin/add_Event.html')

def view_Event(req):

    return render(req, 'myAdmin/view_Event.html')

def edit_Event(req):

    return render(req, 'myAdmin/edit_Event.html')

