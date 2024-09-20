from django.shortcuts import redirect,render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from myApp.models import *


def homePage(req):
    return render(req,'homePage.html')

def logoutPage(req):
    logout(req)
    return redirect("loginPage")
    

def loginPage(req):
    if req.method=='POST':
        Username=req.POST.get('username')
        Password=req.POST.get('password')
        user=authenticate(
            username=Username,
            password=Password,
        )
        if user:
            login(req,user)
        return redirect("homePage")
        
    return render (req,'loginPage.html')

def registerPage(req):
    if req.method=='POST':
        Username=req.POST.get('username')
        Email=req.POST.get('email')
        ContactNo=req.POST.get('contactno')
        Age=req.POST.get('age')
        Password=req.POST.get('password')
        Confirmpassword=req.POST.get('confirmpassword')
        if Password==Confirmpassword:
            user=CustomUser.objects.create_user(
                username=Username,
                email=Email,
                contact_no=ContactNo,
                age=Age,
                password=Confirmpassword
            )
            return redirect("loginPage")
            
            
    return render(req,'registerPage.html')

def addResumePage(req):
    All_User=CustomUser.objects.all()
    
    
    if req.method=='POST':
        
        # Custom_ID=req.POST.get('customuser_id')
        # user_object=get_object_or_404(CustomUser,id=Custom_ID)
        
        
        resume=resumeModel(
            user=get_object_or_404(CustomUser,id=req.POST.get("customuser_id")),
            Designation=req.POST.get('designation'),
            Cotact_number=req.POST.get('cotact_number'),
            Career_summary=req.POST.get('career_summary'),
            Profile_pic=req.POST.get('profile_pic'),
            Gender_type=req.POST.get('gender_type'),
            Linkedin_URL=req.POST.get('linkedin_URL'),
            Facebook_URL=req.POST.get('facebook_URL'),
            Instagram_URL=req.POST.get('instagram_URL'),
            Github_URL=req.POST.get('github_URL'),    
        )
        resume.save()
    
    
    context={
        "All_User":All_User
    }
    
    return render(req, 'addResumePage.html',context)

def resumelistPage(req):
    data=CustomUser.objects.all()
    context={
        'data':data
    }
    return render(req, 'resumelistPage.html',context)


def addSkillPage(req):
    all_user=CustomUser.objects.all()
    Skill_Name=Intermediate_skill_model.objects.all()
    
    if req.method=='POST':
        skill_id=req.POST.get('skill_id')
        skill=SkillModel(
            user=get_object_or_404(CustomUser,id=req.POST.get('USER_ID')),
            sikll_name=get_object_or_404(Intermediate_skill_model,id=skill_id),
            Profiency_level=req.POST.get('profiency_level'),
        )
        skill.save()
    
    context={
        "all_user":all_user,
        "skill_name":Skill_Name,
    }
    return render(req,'addSkillPage.html',context)