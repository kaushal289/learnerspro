from django.shortcuts import render
from pprint import pprint
from django.http import request
from django.shortcuts import redirect, render
import student
from student.models import Student
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from student.forms import StudentForm
# Create your views here.
def studentdashboard(request):
<<<<<<< HEAD
    return render(request,"student/landingpage.html")
=======
    return render(request,"student/landingpage.html")

def register(request):
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST)
        form.save()
        user1=form.cleaned_data.get('username')
        return redirect("/studentlogin")
    else:
        form = StudentForm()
    return render(request, "reglogin/registration.html", {'form': form})

def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('/studentdashboard')
        else:
            messages.error(request, "bad credentials")
            return redirect('/admin/adminlogin')
    return render(request, 'reglogin/login.html')
>>>>>>> 9ce82703edd49e8d7d9918e6e12bfef302f719dc
