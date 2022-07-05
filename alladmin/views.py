import imp
from django.shortcuts import render, redirect
from alladmin.forms import AdminForm
from alladmin.models import Admin
from student.models import Student, Ticket
from teacher.forms import TeacherForm, Teacher
from teacher.models import Teacher
from django.contrib import messages
# Create your views here.
def admindash(request):
    return render(request, "admindashboard.html")

def addadmin(request):
    if request.method == "POST":
        print(request.POST)
        form = AdminForm(request.POST)
        form.save()
        return redirect("/addteacher")
    else:
        form = AdminForm()
    return render(request, "admin/addadmin.html", {'form': form})
def updatepassword(request,s_id):
    admin=Admin.objects.get(admin_id=s_id)
    return render (request, "admin/updatepassword.html",{'admin':[admin]})

def adminupdate(request,s_id):
    admin=Admin.objects.get(admin_id=s_id)
    request.session['admin_id']=admin.admin_id
    form=AdminForm(request.POST, instance=admin)
    form.save()
    return render (request, "admin/updatepassword.html",{'admin':[admin]})

def ticketview(request):
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
    tickets=Ticket.objects.raw('select * from ticket limit 8 offset % s', [offset])
    pageItem = len(tickets)
    return render(request,"admin/tickettable.html", {'tickets':tickets,'page': page, 'pageItem': pageItem})

def ticketdelete(request,t_id):
    ticket=Ticket.objects.get(ticket_id=t_id)
    ticket.delete()
    messages.success(request, "Deleted Successfully")
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
    teachers=Teacher.objects.raw('select * from teacher limit 8 offset % s', [offset])
    pageItem = len(teachers)
    return render(request,"admin/teacherview.html", {'teachers':teachers,'page': page, 'pageItem': pageItem})
def studentview(request):
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
    students=Student.objects.raw('select * from student limit 8 offset % s', [offset])
    pageItem = len(students)
    return render(request,"admin/viewstudent.html", {'students':students,'page': page, 'pageItem': pageItem})

def teacherdelete(request,td_id):
    teacher=Teacher.objects.get(teacher_id=td_id)
    teacher.delete()
    messages.success(request, "Teacher account deleted successfully.")
    return redirect ("/teacherview")

def studentdelete(request,td_id):
    student=Student.objects.get(student_id=td_id)
    student.delete()
    messages.success(request, "Student account deleted successfully.")
    return redirect ("/studentview")
