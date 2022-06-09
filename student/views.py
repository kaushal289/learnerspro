import imp
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
from student.forms import StudentForm, Questionform
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
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            teacher=Teacher.objects.get(username=username,password=password)
            print(teacher)
            if teacher is not None:
                request.session['username']=request.POST['username']
                request.session['password']=request.POST['password'] 
                return render(request,"teacher/landingpage.html")
        except:
            try:
                user=Student.objects.get(username=username,password=password)
                request.session['username']=request.POST['username']
                request.session['password']=request.POST['password']
                request.session['student_id']=user.student_id
                request.session['student_id']=user.student_id
                users=Student.objects.get(student_id=request.session['student_id'])
                return render(request,"student/landingpage.html",{'users':[users]})
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
    users=Student.objects.get(student_id=request.session['student_id'])
    return render(request, "student/studentsubject.html",{'users':[users]})

def questionanswer(request):
    return render(request, "student/qa.html")

def question(request):
    if request.method == "POST":
        print(request.POST)
        form = Questionform(request.POST,request.FILES)
        if (form.is_valid()):            
            form.save()
            print('Fromn Saved')
            return redirect("/question")
    else:
        form = Questionform()
    return render(request, "student/question.html", {'form': form})
    


