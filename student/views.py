<<<<<<< HEAD
import imp
=======
from asyncio.log import logger
>>>>>>> c163024aba3038eb84a3109dd5345932d92f0255
from django.shortcuts import render
from pprint import pprint
from django.http import JsonResponse, request
from django.shortcuts import redirect, render
import os
from django.views import View
from student.models import Student
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from student.forms import StudentForm
from teacher.models import Teacher
from django.contrib import messages, auth
# Create your views here.
def studentdashboard(request):
    try:
        users=Student.objects.get(student_id=request.session['student_id'])
        return render(request,"student/landingpage.html",{'users':[users]})
    except:
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
<<<<<<< HEAD
            teacher=Teacher.objects.get(username=username,password=password)
            print(teacher)
            if teacher is not None:
                request.session['username']=request.POST['username']
                request.session['password']=request.POST['password'] 
                return render(request,"teacher/landingpage.html")
=======
            users=Student.objects.get(username=username,password=password)
            print(users)
            if users is not None:
                request.session['username']=request.POST['username']
                request.session['password']=request.POST['password']
                request.session['student_id']=users.student_id
                users=Student.objects.get(student_id=request.session['student_id'])
                return render(request,"student/landingpage.html",{'users':[users]})
>>>>>>> c163024aba3038eb84a3109dd5345932d92f0255
                
        except:
            try:  
                user=Student.objects.get(username=username,password=password)
                request.session['username']=request.POST['username']
                request.session['password']=request.POST['password']
                request.session['student_id']=user.student_id
                print("1")
                request.session['student_id']=user.student_id
                return render(request,"student/landingpage.html")
            except:
                messages.error(request, 'Please enter correct username and password')
                return render(request,"reglogin/login.html")
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
    return render(request,"student/profile.html",{'users':[users]})

def profileupdate(request,s_id):
    student=Student.objects.get(student_id=s_id)
    if request.method=="POST":
        try:
            if len(request.FILES) != 0:
                if len(student.image)>0:
                    os.remove(student.image.path)
                student.image=request.FILES['image']
        except:
            student.image=request.FILES['image']
    form=StudentForm(request.POST, instance=student)
    form.save()
    request.session['username']=request.POST['username']
    users=Student.objects.get(student_id=s_id)
    return render(request,"student/profile.html",{'users':[users]})

def studentsubject(request):
    return render(request, "student/studentsubject.html")




