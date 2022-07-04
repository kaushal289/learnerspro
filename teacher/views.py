from select import select
from django.shortcuts import render, redirect
from student.forms import Questionform
from teacher.models import Teacher
from teacher.forms import TeacherForm
import os


from addcourse.forms import *
from addcourse.models import *
from student.models import Question

# Create your views here.
def register(request):
    if request.method == "POST":
        print(request.POST)
        form = TeacherForm(request.POST)
        form.save()
        return redirect("/studentlogin")
    else:
        form = TeacherForm()
    return render(request, "reglogin/teacherregistration.html", {'form': form})

def teacherdashboard(request):
    return render(request,"teacher/landingpage.html")


def logout(request):
    request.session.clear()
    return redirect('/')

def teacherprofile(request,s_id):
    users=Teacher.objects.get(teacher_id=s_id)
    return render(request,"teacher/teacherprofile.html",{'users':[users]})
   
def profileupdateteacher(request,s_id):
    users=Teacher.objects.get(teacher_id=s_id)
    form=TeacherForm(request.POST, instance=users)
    form.save()
    return render(request,"teacher/teacherprofile.html",{'users':[users]})

def addsubjectpage(request):
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

def answer(request,a_id):
    try:
        course=Course.objects.get(course_id=a_id)
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

def questionview(request):
    print(request)
    if (request.method == "POST"):
        page = int(request.POST['page'])
        if ('prev' in request.POST):
            page = page - 1
        if ('next' in request.POST):
            page = page + 1
        tempOffSet = page - 1
        offset = tempOffSet * 6
        print(offset)
    else:
        offset = 0
        page = 1
    questions=Question.objects.raw('select * from question limit 6 offset % s', [offset])
    pageItem = len(questions)
    return render(request,"teacher/questiontable.html", {'questions':questions,'page': page, 'pageItem': pageItem})

def questiondelete(request,q_id):
    question=Question.objects.get(question_id=q_id)
    question.delete()
    return redirect ("/questionview")
def editquestion(request,q_id):
    try:
        question=Question.objects.get(question_id=q_id)
        return render(request, "teacher/answer.html", {'question':question})
    except:
        print("No Data Found")
    return redirect ("/questionview")
def updatequestion(request,q_id):
    question=Question.objects.get(question_id=q_id)
    form=Questionform(request.POST, instance=question)
    form.save()
    return redirect ("/questionview")
