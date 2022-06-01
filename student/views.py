from ast import Pass
from cmath import log
from django.http import HttpResponseRedirect
from django.shortcuts import render
from pprint import pprint
from django.shortcuts import redirect, render
import os
from authenticate import Authentication
from pkg_resources import require
from addcourse.models import Course
from student.models import Question, Student
from alladmin.models import Admin
from django.contrib import messages
from student.forms import StudentForm, Questionform, TicketForm
from teacher.models import Teacher
from django.contrib import messages
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str, force_bytes, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.contrib.auth import logout as do_logout



def studentdashboard(request):
    
    # print (request.session.username)
    # print(request.session.username)
    # print(reque
    # st.user.username)
    print('hello')
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
                request.session.set_expiry(0)
                request.session['username']=request.POST['username']
                request.session['password']=request.POST['password'] 
                request.session['teacher_id']=teacher.teacher_id
                return render(request,"teacher/addsubject.html")
           
            
        except:
            try:
                user=Student.objects.get(username=username,password=password)
                request.session.set_expiry(0)
                request.session['username']=request.POST['username']
                request.session['password']=request.POST['password']
                request.session['student_id']=user.student_id
                request.session['exists'] = True
                users=Student.objects.get(student_id=request.session['student_id'])
                
                return render(request,"student/landingpage.html",{'users':[users]})
                
            except:
                try:
                    admin=Admin.objects.get(username=username,password=password)
                    if admin is not None:
                        request.session.set_expiry(0)
                        request.session['username']=request.POST['username']
                        request.session['password']=request.POST['password'] 
                        request.session['admin_id']=admin.admin_id
                        return render(request,"admin/addteacher.html")
                except:
                    Pass 
                messages.error(request, 'Please enter correct username and password')
                return render(request,"reglogin/login.html")
  
            
    else:
        form=StudentForm()
        print("invalid")
        request.session['exists'] = False
    return render(request,"reglogin/login.html",{'form':form}) 


def logout(request):
    do_logout(request)
    # request.session.clear()
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
@Authentication.valid_user
def class6(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    return render(request, "class6/class6.html",{'users':[users]})
@Authentication.valid_user
def class7(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    return render(request, "class7/class7.html",{'users':[users]})
@Authentication.valid_user
def class8(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    return render(request, "class8/class8.html",{'users':[users]})
@Authentication.valid_user
def class9(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    return render(request, "class9/class9.html",{'users':[users]})
@Authentication.valid_user
def class10(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    return render(request, "class10/class10.html",{'users':[users]})
@Authentication.valid_user
def class6science(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    sciences=Course.objects.raw("select * from course where std_class='6' and subject='Science'")
    return render(request, "class6/class6science.html",{'users':[users],'sciences':sciences})
@Authentication.valid_user
def class7science(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    sciences=Course.objects.raw("select * from course where std_class='7' and subject='Science'")
    return render(request, "class7/class7science.html",{'users':[users],'sciences':sciences})


@Authentication.valid_user
def class8science(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    sciences=Course.objects.raw("select * from course where std_class='8' and subject='Science'")
    return render(request, "class8/class8science.html",{'users':[users],'sciences':sciences})
@Authentication.valid_user
def class9science(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    sciences=Course.objects.raw("select * from course where std_class='9' and subject='Science'")
    return render(request, "class9/class9science.html",{'users':[users],'sciences':sciences})
@Authentication.valid_user
def class10science(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    sciences=Course.objects.raw("select * from course where std_class='10' and subject='Science'")
    return render(request, "class10/class10science.html",{'users':[users],'sciences':sciences})
@Authentication.valid_user
def class6english(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    englishs=Course.objects.raw("select * from course where std_class='6' and subject='English'")
    return render(request, "class6/class6english.html",{'users':[users],'englishs':englishs})
@Authentication.valid_user
def class7english(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    englishs=Course.objects.raw("select * from course where std_class='7' and subject='English'")
    return render(request, "class7/class7english.html",{'users':[users],'englishs':englishs})
@Authentication.valid_user
def class8english(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    englishs=Course.objects.raw("select * from course where std_class='8' and subject='English'")
    return render(request, "class8/class8english.html",{'users':[users],'englishs':englishs})
@Authentication.valid_user
def class9english(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    englishs=Course.objects.raw("select * from course where std_class='9' and subject='English'")
    return render(request, "class9/class9english.html",{'users':[users],'englishs':englishs})
@Authentication.valid_user
def class10english(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    englishs=Course.objects.raw("select * from course where std_class='10' and subject='English'")
    return render(request, "class10/class10english.html",{'users':[users],'englishs':englishs})
@Authentication.valid_user
def class6math(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    maths=Course.objects.raw("select * from course where std_class='6' and subject='Maths'")
    return render(request, "class6/class6math.html",{'users':[users],'maths':maths})

@Authentication.valid_user
def class7math(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    maths=Course.objects.raw("select * from course where std_class='7' and subject='Maths'")
    return render(request, "class7/class7math.html",{'users':[users],'maths':maths})
@Authentication.valid_user
def class8math(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    maths=Course.objects.raw("select * from course where std_class='8' and subject='Maths'")
    return render(request, "class8/class8math.html",{'users':[users],'maths':maths})
@Authentication.valid_user
def class9math(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    maths=Course.objects.raw("select * from course where std_class='9' and subject='Maths'")
    return render(request, "class9/class9math.html",{'users':[users],'maths':maths})
@Authentication.valid_user
def class10math(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    maths=Course.objects.raw("select * from course where std_class='10' and subject='Maths'")
    return render(request, "class10/class10math.html",{'users':[users],'maths':maths})
@Authentication.valid_user
def class6computer(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    computers=Course.objects.raw("select * from course where std_class='6' and subject='Computer'")
    return render(request, "class6/class6computer.html",{'users':[users],'computers':computers})
@Authentication.valid_user
def class7computer(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    computers=Course.objects.raw("select * from course where std_class='7' and subject='Computer'")
    return render(request, "class7/class7computer.html",{'users':[users],'computers':computers})
@Authentication.valid_user
def class8computer(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    computers=Course.objects.raw("select * from course where std_class='8' and subject='Computer'")
    return render(request, "class8/class8computer.html",{'users':[users],'computers':computers})
@Authentication.valid_user
def class9computer(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    computers=Course.objects.raw("select * from course where std_class='9' and subject='Computer'")
    return render(request, "class9/class9computer.html",{'users':[users],'computers':computers})
@Authentication.valid_user
def class10computer(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    computers=Course.objects.raw("select * from course where std_class='10' and subject='Computer'")
    return render(request, "class10/class10computer.html",{'users':[users],'computers':computers})


@Authentication.valid_user
def class6social(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    socials=Course.objects.raw("select * from course where std_class='6' and subject='Social studies'")
    return render(request, "class6/class6social.html",{'users':[users],'socials':socials})
@Authentication.valid_user
def class7social(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    socials=Course.objects.raw("select * from course where std_class='7' and subject='Social studies'")
    return render(request, "class7/class7social.html",{'users':[users],'socials':socials})
@Authentication.valid_user
def class8social(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    socials=Course.objects.raw("select * from course where std_class='8' and subject='Social studies'")
    return render(request, "class8/class8social.html",{'users':[users],'socials':socials})
@Authentication.valid_user
def class9social(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    socials=Course.objects.raw("select * from course where std_class='9' and subject='Social studies'")
    return render(request, "class9/class9social.html",{'users':[users],'socials':socials})
@Authentication.valid_user
def class10social(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    socials=Course.objects.raw("select * from course where std_class='10' and subject='Social studies'")
    return render(request, "class10/class10social.html",{'users':[users],'socials':socials})


@Authentication.valid_user
def class7account(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    accounts=Course.objects.raw("select * from course where std_class='7' and subject='Accounts'")
    return render(request, "class7/class7account.html",{'users':[users],'accounts':accounts})

@Authentication.valid_user
def class9account(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    accounts=Course.objects.raw("select * from course where std_class='9' and subject='Accounts'")
    return render(request, "class9/class9account.html",{'users':[users],'accounts':accounts})
@Authentication.valid_user
def class10account(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    accounts=Course.objects.raw("select * from course where std_class='10' and subject='Accounts'")
    return render(request, "class10/class10account.html",{'users':[users],'accounts':accounts})



@Authentication.valid_user
def questionanswer(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    return render(request, "student/qa.html",{'users':[users]})

def question(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    if request.method == "POST":
        print(request.POST)
        form = Questionform(request.POST,request.FILES)
        if (form.is_valid()):            
            form.save()
            print('Fromn Saved')
            return redirect("/questionanswer")
    else:
        form = Questionform()
    return render(request, "student/question.html", {'users':[users],'form': form})

def ticket(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    if request.method == "POST":
        print(request.POST)
        form = TicketForm(request.POST,request.FILES)
        if (form.is_valid()):
            form.save()
            print('Fromn Saved')
            return redirect("/")
    else:
        form = TicketForm()
    return render(request, "student/ticket.html", {'form': form,'users':[users]})
    
#forget password

def send_forget_password_email(request, user):

    subject = "Reset password link"

    if request.method == "POST":

        email = request.POST.get('email')

    current_site = get_current_site(request)

    email_body = render_to_string('student/clicklink.html', {

        'user': user,

        'domain': current_site,

        'uid': urlsafe_base64_encode(force_bytes(user.pk)),

        'token': generate_token.make_token(user),



    })

    email = EmailMessage(subject=subject,

    body=email_body,

    from_email= settings.EMAIL_FROM_USER,

    to=[user.email]

    )
    email.send()

def enter_email(request):

    if request.method == 'POST':

        email = request.POST.get('email')

        if not Student.objects.filter(email=email):

            messages.success(request, 'User not registered')

        else:

            user = Student.objects.get(email=email)

            print (user.username)

            send_forget_password_email(request, user)


    return render(request, 'student/enteremail.html')

def clicklink(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Student.objects.get(pk=uid)
    except Exception as e:
        user = None
    if user and generate_token.check_token(user, token):
        return redirect('resetpassword', pk=user.student_id)


def reset_password(request, pk):
    user = Student.objects.get(student_id=pk)
    if request.method == 'POST':
         password = request.POST.get("new_password")
         cpassword = request.POST.get("confirm_password")

         if password == cpassword:
             user.password = password
             user.save()

             return redirect('studentlogin')

    return render(request, "student/resetpassword.html")

def getanswer(request):
    users=Student.objects.get(student_id=request.session['student_id'])
    answers=Question.objects.filter(student=request.session['student_id'])
    return render(request,"student/getanswer.html", {'users':[users],'answers':answers})

