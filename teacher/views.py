from django.shortcuts import render, redirect
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

def teachersubject(request):
    return render(request, "teacher/teachersubject.html")

def logout(request):
    request.session.clear()
    return redirect('/')

def addsubject(request):
    if request.method == "POST":
        form = teachersubject(request.POST, request.FILES)
        form.save()
        return redirect("/teachersubject")
    return render(request, "teacher/addsubject.html")


def email(request):
    return render (request, "teacher/email.html")


def reset(request):
    return render (request, "teacher/resetpassword.html")