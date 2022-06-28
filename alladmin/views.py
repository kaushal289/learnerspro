from django.shortcuts import render, redirect
from student.models import Ticket
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
