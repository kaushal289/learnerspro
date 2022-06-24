from django.shortcuts import render, redirect
from teacher.models import Teacher
from teacher.forms import TeacherForm
import os

from addcourse.forms import *
from addcourse.models import *

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

def allcourse(request):
    if (request.method == "POST"):
        page = int(request.POST['page'])
        if ('prev' in request.POST):
            page = page - 1
        if ('next' in request.POST):
            page = page + 1
        tempOffSet = page - 1
        offset = tempOffSet * 8
        print(offset)
    else:
        offset = 0
        page = 1
    
    courses=Course.objects.raw('select * from course limit 8 offset % s', [offset])
    pageItem = len(courses)
    return render(request,"teacher/viewallcources.html",{'courses':courses, 'page': page, 'pageItem': pageItem})

def editcourse(request,c_id):
    try:
        course=Course.objects.get(course_id=c_id)
        print(course)
        return render(request, "teacher/editcourse.html", {'course':course})
    except:
        print("No Data Found")
    return redirect ("/allcourse")

def courseupdate(request,c_id):
    course=Course.objects.get(course_id=c_id)
    if request.method=="POST":
        if len(request.FILES) != 0:
            if len(course.content)>0:
                os.remove(course.content.path)
            course.content=request.FILES['content']
    
    form=Courseform(request.POST, instance=course)
    form.save()
    return redirect ("/allcourse")

def deletecourse(request,c_id):
    course=Course.objects.get(course_id=c_id)
    course.delete()
    return redirect ("/allcourse")