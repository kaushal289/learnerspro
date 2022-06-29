from django.shortcuts import render, redirect
from student.models import Ticket
from teacher.forms import TeacherForm, Teacher
from teacher.models import Teacher
# Create your views here.
def admindash(request):
    return render(request, "admindashboard.html")

<<<<<<< HEAD
def updatepassword(request):
    return render (request, "admin/updatepassword.html")

=======
def ticketview(request):
    print(request)
    tickets=Ticket.objects.raw('select * from ticket')
    return render(request,"admin/tickettable.html", {'tickets':tickets})
>>>>>>> 0a75ca3717b602bd05567c0daefc1309c0e09115

def ticketdelete(request,t_id):
    ticket=Ticket.objects.get(ticket_id=t_id)
    ticket.delete()
    return redirect ("/ticketview")

def addteacher(request):
    if request.method == "POST":
        print(request.POST)
        form = TeacherForm(request.POST)
        form.save()
        user1=form.cleaned_data.get('username')
        return redirect("/teacherview")
    else:
        form = TeacherForm()
    return render(request, "admin/addteacher.html", {'form': form})

def teacherview(request):
    print(request)
    teachers=Teacher.objects.raw('select * from teacher')
    return render(request,"admin/removeteacher.html", {'teachers':teachers})

def teacherdelete(request,td_id):
    teacher=Teacher.objects.get(teacher_id=td_id)
    teacher.delete()
    return redirect ("/teacherview")
