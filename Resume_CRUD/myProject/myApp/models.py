from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER=[
        ('admin','Admin'),
        ('viewer','Viewer'),
    ]
    
    user_type=models.CharField(max_length=100, null=True,choices=USER)
    age=models.PositiveIntegerField(null=True)
    contact_no=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f"{self.first_name}-{self.last_name}-{self.age}"
    
class resumeModel(models.Model):
        GENDER=[
            ('male','Male'),
            ('female','Female'),
            ('others','Others'),
        ]
        user=models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE)
        Designation=models.CharField(max_length=100, null=True)
        cotact_number=models.CharField(max_length=100,null=True)
        Career_Summary=models.CharField(max_length=100,null=True)
        Profile_pic=models.ImageField(upload_to="Medis/Profile_pic",null=True)
        
        Linkedin_URL=models.URLField(max_length=100,null=True)
        Facebook_URL=models.URLField(max_length=100,null=True)
        Instagram_URL=models.URLField(max_length=100,null=True)
        Github_URL=models.URLField(max_length=100,null=True)
        
        gender_type=models.CharField(max_length=100,null=True,choices=GENDER)
        
        def __str__(self):
            return f"{self.Designation}-{self.user.usernmame}"
        
class EducationModel(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True)
    start_year=models.DateField(max_length=100,null=True)
    ecd_year=models.DateField(max_length=100,null=True)
            
    def __str__(self):
        return f"{self.user.username}-{self.title}"
    
class SkillModel(models.Model):
    
    PROFIENCY=[
        ('high','High'),
        ('mideum','Mideum'),
        ('low','Low'),
    ]
    
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    
    sikll_name=models.CharField(max_length=100,null=True)
    
    Profiency_level=models.CharField(max_length=100,null=True,choices=PROFIENCY)
    
    def __str__(self):
        return f"{self.user.username}-{self.sikll_name}"
    
    
class ExperienceModel(models.Model):
    
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    
    title=models.CharField(max_length=100,null=True)
    Start_date=models.DateField(max_length=100,null=True)
    End_date=models.DateField(max_length=100,null=True)
    Description=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        
        return f"{self.user.username}-{self.title}"

    
class InterestModel(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    Interest_name=models.CharField(max_length=100,null=True)
    
    
    def __str__(self):
        return f"{self.user.username}-{self.Interest_name}"
    
class languageModel(models.Model):
    
    PROFIENCY=[
        ('high','High'),
        ('mideum','Mideum'),
        ('low','Low'),
    ] 
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    
    language_name=models.CharField(max_length=100,null=True)
    Profiency_level=models.CharField(max_length=100,null=True,choices=PROFIENCY)
    
    def __str__(self):
        return f"{self.user.username}-{self.language_name}"  
    
    
    
class Intermediate_skill_model(models.Model):
    Skill_name=models.CharField(max_length=100,null=True) 
    
    def __str__(self):
        return f"{self.Skill_name}"
        
        
    
