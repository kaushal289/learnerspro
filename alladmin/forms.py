from django import forms 
from alladmin.models import *
from teacher.models import *

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"

class TeacherForm(forms.ModelForm):    
    class Meta:
        model = Teacher
        fields = ("teacher_firstname","teacher_lastname","username","email","phone_number","password")