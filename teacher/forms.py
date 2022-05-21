from django import forms 
from teacher.models import Teacher

class TeacherForm(forms.ModelForm):    
    class Meta:
        model = Teacher
        fields = ("teacher_firstname","teacher_lastname","username","email","phone_number","password")