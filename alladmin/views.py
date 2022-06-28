from django.shortcuts import render, redirect
from student.models import Ticket
from teacher.forms import TeacherForm
# Create your views here.
def admindash(request):
    return render(request, "admindashboard.html")

def ticketview(request):
    print(request)
    tickets=Ticket.objects.raw('select * from ticket')
    return render(request,"admin/tickettable.html", {'tickets':tickets})

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
        return redirect("/admindash")
    else:
        form = TeacherForm()
    return render(request, "admin/addteacher.html", {'form': form})
