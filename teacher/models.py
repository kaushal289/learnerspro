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

