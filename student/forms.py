from django import forms 
from student.models import Student, Question, Ticket


class StudentForm(forms.ModelForm):    
    class Meta:
        model = Student
        fields = ("student_firstname","student_lastname","username","phone_number","email","password","image")

class Questionform(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"