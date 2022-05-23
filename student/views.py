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
                return render(request,"student/landingpage.html")
                
        except:
                print("2")
                messages.error(request, 'Please enter correct username and password')
                return render(request,"reglogin/login.html")
    else:
        form=StudentForm()
        print("invalid")
    return render(request,"reglogin/login.html",{'form':form}) 

def logout(request):
    request.session.clear()
    return redirect('/')

def profile(request):
    users=Student.objects.get(id=request.session['id'])
    print(users)
    return render(request,"student/userprofile.html",{'users':[users]})

def updateprofile(request,p_id):
    student=Student.objects.get(id=p_id)
    form=StudentForm(request.POST, instance=student)
    form.save()
    return redirect("/userprofile.html")
