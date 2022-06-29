from django.shortcuts import render
# Create your views here.
def admindash(request):
    return render(request, "admindashboard.html")

def updatepassword(request):
    return render (request, "admin/updatepassword.html")


