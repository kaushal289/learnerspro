from django.shortcuts import render

# Create your views here.
def studentdashboard(request):
    return render(request,"student/landingpage.html")