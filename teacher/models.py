from django import db
from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id=models.AutoField(auto_created=True, primary_key=True)
    teacher_firstname=models.CharField(max_length=100)
    teacher_lastname=models.CharField(max_length=200)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
    last_login=models.DateTimeField(null=True)
    

    class Meta:
        db_table="teacher"
        
class Teachersubject(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset()
        
    subject_id = models.AutoField(auto_created=True, primary_key=True)
    subject_name = models.CharField(max_length=100, blank=True)
    subject_desc = models.CharField(max_length=250, blank=True)
    s_genre=models.CharField(max_length=100, blank=True)
    s_pic= models.FileField(upload_to='books', blank=True)
    objects=models.Manager() #default manager
    newmanager= NewManager() #custom manager

    class Meta:
        db_table="teachersubject"
    