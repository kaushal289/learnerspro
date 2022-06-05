from django.shortcuts import render
from pprint import pprint
from django.http import request
from django.shortcuts import redirect, render
import os
from student.models import Student
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from student.forms import StudentForm
from teacher.models import Teacher
# Create your views here.
def studentdashboard(request):
    return render(request,"student/landingpage.html")

def register(request):
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST,request.FILES)
        form.save()
        return redirect("/studentlogin")
    else:
        form = StudentForm()
    return render(request, "reglogin/registration.html", {'form': form})

def studentlogin(request):
    print("12345")
    if request.method=='POST':
        print(request)
        print("1")
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            user=Student.objects.get(username=username,password=password)
            print(user)
            if user is not None:
                request.session['username']=request.POST['username']
                request.session['password']=request.POST['password'] 
                print("1")
                request.session['student_id']=user.student_id
                return render(request,"student/landingpage.html")
                
        except:
            try:  
                teacher=Teacher.objects.get(username=username,password=password)
                request.session['username']=request.POST['username']
                request.session['password']=request.POST['password']
                request.session['teacher_id']=teacher.teacher_id
                return render(request,"teacher/landingpage.html")
            except:
                messages.error(request, 'Please enter correct username and password')
                return render(request,"auth/login.html")
    else:
        form=StudentForm()
        print("invalid")
    return render(request,"reglogin/login.html",{'form':form}) 


def logout(request):
    request.session.clear()
    return redirect('/')

def studentprofile(request,s_id):
    try:
        users=Student.objects.get(student_id=s_id)
        return render(request,"student/profile.html",{'users':[users]})
    except:
        print("No Data Found")
    return redirect ("/useradmin/adminproduct")

def profileupdate(request,s_id):
    student=Student.objects.get(student_id=s_id)
    if request.method=="POST":
            student.image=request.FILES['image']
    form=StudentForm(request.POST, instance=student)
    form.save()
    request.session['username']=request.POST['username']
    users=Student.objects.get(student_id=s_id)
    return render(request,"student/profile.html",{'users':[users]})




