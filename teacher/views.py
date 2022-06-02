from django.shortcuts import render, redirect
from numpy import product
from teacher.models import Teacher
from teacher.forms import TeacherForm

# Create your views here.
def register(request):
    if request.method == "POST":
        print(request.POST)
        form = TeacherForm(request.POST)
        form.save()
        user1=form.cleaned_data.get('username')
        return redirect("/studentlogin")
    else:
        form = TeacherForm()
    return render(request, "reglogin/teacherregistration.html", {'form': form})

def teacherdashboard(request):
    return render(request,"teacher/landingpage.html")
