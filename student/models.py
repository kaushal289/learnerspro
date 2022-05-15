from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    student_firstname=models.CharField(max_length=100)
    student_lastname=models.CharField(max_length=200)
    username=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    last_login=models.DateTimeField(null=True)
    

    class Meta:
        db_table="student"