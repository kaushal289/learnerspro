from django import forms 
from student.models import Student

class StudentForm(forms.ModelForm):    
    class Meta:
        model = Student
        fields = ("student_firstname","student_lastname","phone_number","email","password")