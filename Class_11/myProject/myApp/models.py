from django.db import models

class eventModel(models.Model):
    
    Gender={
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    }
    first_name=models.CharField(max_length=100, null=True)
    last_name=models.CharField(max_length=100, null=True)
    event_id=models.CharField(max_length=100, null=True)
    gender=models.CharField(max_length=100,choices=Gender, null=True)
    dob=models.DateField(max_length=100, null=True)
    Class=models.CharField(max_length=100, null=True)
    religon=models.CharField(max_length=100, null=True)
    joining_date=models.DateField(max_length=100, null=True)
    mobile_number=models.CharField(max_length=100, null=True)
    addmission_number=models.IntegerField(null=True)
    section=models.CharField(max_length=100, null=True)
    student_img=models.ImageField(upload_to="Media/stu_img", null=True)
    father_name=models.CharField(max_length=100, null=True)
    father_occupation=models.CharField(max_length=100, null=True)
    father_number=models.CharField(max_length=100, null=True)
    father_email=models.EmailField(max_length=100, null=True)
    mother_name=models.CharField(max_length=100, null=True)
    mother_occuoation=models.CharField(max_length=100, null=True)
    mother_number=models.CharField(max_length=100, null=True)
    mother_email=models.EmailField(max_length=100, null=True)
    present_address=models.CharField(max_length=100, null=True)
    permanent_address=models.CharField(max_length=100, null=True)
    
    
