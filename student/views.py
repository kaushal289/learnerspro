from ast import Pass
from django.http import HttpResponseRedirect
from django.shortcuts import render
from pprint import pprint
from django.shortcuts import redirect, render
import os
from addcourse.models import Course
from student.models import Student
from alladmin.models import Admin
from django.contrib import messages
from student.forms import StudentForm, Questionform, TicketForm
from teacher.models import Teacher
from django.contrib import messages
# Create your views here.
def studentdashboard(request):
    try:
        users=Student.objects.get(student_id=request.session['student_id'])
        return render(request,"student/landingpage.html",{'users':[users]})
    except:
        return render(request,"student/landingpage.html")

def register(request):
    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES)
        username=request.POST["username"]
        try:
            Student.objects.get(username=username)
            messages.error(request, 'Username already used')
            return redirect(request.META['HTTP_REFERER'])
        except:
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
            print("A")
           
            teacher=Teacher.objects.get(username=username,password=password)
           
            print("B")
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
                try:
                    admin=Admin.objects.get(username=username,password=password)
                    if admin is not None:
                        request.session['username']=request.POST['username']
                        request.session['password']=request.POST['password'] 
                        return render(request,"admindashboard.html")
                except:
                    Pass 
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

def class6(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    return render(request, "class6/class6.html",{'users':[users]})

def class7(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    return render(request, "class7/class7.html",{'users':[users]})

def class8(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    return render(request, "class8/class8.html",{'users':[users]})

def class9(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    return render(request, "class9/class9.html",{'users':[users]})

def class10(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    return render(request, "class10/class10.html",{'users':[users]})

def class6science(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    sciences=Course.objects.raw("select * from course where std_class='6' and subject='Science'")
    return render(request, "class6/class6science.html",{'users':[users],'sciences':sciences})

def class7science(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    sciences=Course.objects.raw("select * from course where std_class='7' and subject='Science'")
    return render(request, "class7/class7science.html",{'users':[users],'sciences':sciences})


def class8science(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    sciences=Course.objects.raw("select * from course where std_class='8' and subject='Science'")
    return render(request, "class8/class8science.html",{'users':[users],'sciences':sciences})

def class9science(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    sciences=Course.objects.raw("select * from course where std_class='9' and subject='Science'")
    return render(request, "class9/class9science.html",{'users':[users],'sciences':sciences})

def class10science(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    sciences=Course.objects.raw("select * from course where std_class='10' and subject='Science'")
    return render(request, "class10/class10science.html",{'users':[users],'sciences':sciences})


def class6english(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    englishs=Course.objects.raw("select * from course where std_class='6' and subject='English'")
    return render(request, "class6/class6english.html",{'users':[users],'englishs':englishs})

def class7english(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    englishs=Course.objects.raw("select * from course where std_class='7' and subject='English'")
    return render(request, "class7/class7english.html",{'users':[users],'englishs':englishs})

def class8english(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    englishs=Course.objects.raw("select * from course where std_class='8' and subject='English'")
    return render(request, "class8/class8english.html",{'users':[users],'englishs':englishs})

def class9english(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    englishs=Course.objects.raw("select * from course where std_class='9' and subject='English'")
    return render(request, "class9/class9english.html",{'users':[users],'englishs':englishs})

def class10english(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    englishs=Course.objects.raw("select * from course where std_class='10' and subject='English'")
    return render(request, "class10/class10english.html",{'users':[users],'englishs':englishs})

def class6math(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    maths=Course.objects.raw("select * from course where std_class='6' and subject='Maths'")
    return render(request, "class6/class6math.html",{'users':[users],'maths':maths})


def class7math(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    maths=Course.objects.raw("select * from course where std_class='7' and subject='Maths'")
    return render(request, "class7/class7math.html",{'users':[users],'maths':maths})

def class8math(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    maths=Course.objects.raw("select * from course where std_class='8' and subject='Maths'")
    return render(request, "class8/class8math.html",{'users':[users],'maths':maths})

def class9math(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    maths=Course.objects.raw("select * from course where std_class='9' and subject='Maths'")
    return render(request, "class9/class9math.html",{'users':[users],'maths':maths})

def class10math(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    maths=Course.objects.raw("select * from course where std_class='10' and subject='Maths'")
    return render(request, "class10/class10math.html",{'users':[users],'maths':maths})

def class6computer(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    computers=Course.objects.raw("select * from course where std_class='6' and subject='Computer'")
    return render(request, "class6/class6computer.html",{'users':[users],'computers':computers})

def class7computer(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    computers=Course.objects.raw("select * from course where std_class='7' and subject='Computer'")
    return render(request, "class7/class7computer.html",{'users':[users],'computers':computers})

def class8computer(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    computers=Course.objects.raw("select * from course where std_class='8' and subject='Computer'")
    return render(request, "class8/class8computer.html",{'users':[users],'computers':computers})

def class9computer(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    computers=Course.objects.raw("select * from course where std_class='9' and subject='Computer'")
    return render(request, "class9/class9computer.html",{'users':[users],'computers':computers})

def class10computer(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    computers=Course.objects.raw("select * from course where std_class='10' and subject='Computer'")
    return render(request, "class10/class10computer.html",{'users':[users],'computers':computers})



def class6social(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    socials=Course.objects.raw("select * from course where std_class='6' and subject='Social studies'")
    return render(request, "class6/class6social.html",{'users':[users],'socials':socials})

def class7social(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    socials=Course.objects.raw("select * from course where std_class='7' and subject='Social studies'")
    return render(request, "class7/class7social.html",{'users':[users],'socials':socials})

def class8social(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    socials=Course.objects.raw("select * from course where std_class='8' and subject='Social studies'")
    return render(request, "class8/class8social.html",{'users':[users],'socials':socials})

def class9social(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    socials=Course.objects.raw("select * from course where std_class='9' and subject='Social studies'")
    return render(request, "class9/class9social.html",{'users':[users],'socials':socials})

def class10social(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    socials=Course.objects.raw("select * from course where std_class='10' and subject='Social studies'")
    return render(request, "class10/class10social.html",{'users':[users],'socials':socials})


def class7account(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    accounts=Course.objects.raw("select * from course where std_class='7' and subject='Accounts'")
    return render(request, "class7/class7account.html",{'users':[users],'accounts':accounts})


def class9account(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    accounts=Course.objects.raw("select * from course where std_class='9' and subject='Accounts'")
    return render(request, "class9/class9account.html",{'users':[users],'accounts':accounts})

def class10account(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    accounts=Course.objects.raw("select * from course where std_class='10' and subject='Accounts'")
    return render(request, "class10/class10account.html",{'users':[users],'accounts':accounts})




def questionanswer(request):
    return render(request, "student/qa.html")

def question(request):
    if request.method == "POST":
        print(request.POST)
        form = Questionform(request.POST,request.FILES)
        if (form.is_valid()):            
            form.save()
            print('Fromn Saved')
            return redirect("/questionanswer")
    else:
        form = Questionform()
    return render(request, "student/question.html", {'form': form})

def ticket(request):
    if request.method == "POST":
        print(request.POST)
        form = TicketForm(request.POST,request.FILES)
        if (form.is_valid()):
            form.save()
            print('Fromn Saved')
            return redirect("/")
    else:
        form = TicketForm()
    return render(request, "student/ticket.html", {'form': form})
    


