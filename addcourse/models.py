from django.db import models

# Create your models here.
class Course(models.Model):
    course_id=models.AutoField(auto_created=True, primary_key=True)
    std_class=models.CharField(max_length=100)
    subject=models.CharField(max_length=200)
    topic=models.CharField(max_length=100)
    content=models.FileField(upload_to='image',blank=True)
    class Meta:
        db_table="course"
