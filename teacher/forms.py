from django import forms 
from teacher.models import *

class TeacherForm(forms.ModelForm):    
    class Meta:
        model = Teacher
        fields = ("teacher_firstname","teacher_lastname","username","email","phone_number","password")

class addsubject(forms.ModelForm):
    class Meta:
        model = Teachersubject
        fields = ("__all__")

