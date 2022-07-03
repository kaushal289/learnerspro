from django.shortcuts import render,redirect
from addcourse.forms import *
from addcourse.models import *

# Create your views here.
def addcourse(request):
    if request.method == "POST":
        print(request.POST)
        form = Courseform(request.POST,request.FILES)
        form.save()
        return redirect("/allcourse")
    else:
        form = Courseform()
    return render(request, "teacher/addsubject.html", {'form': form})