from django.shortcuts import render, redirect
from numpy import product
from teacher.models import Teacher
from teacher.forms import TeacherForm

# Create your views here.
def register(request):
    if request.method == "POST":
        print(request.POST)
        form = TeacherForm(request.POST)
        form.save()
        user1=form.cleaned_data.get('username')
        return redirect("/studentlogin")
    else:
        form = TeacherForm()
    return render(request, "reglogin/teacherregistration.html", {'form': form})

def teacherdashboard(request):
<<<<<<< HEAD
    return render(request,"teacher/landingpage.html")
=======
    return render(request, "teacherdashboard.html")

def teachersubject(request):
    return render(request, "teacher/teachersubject.html")

def addsubject(request):
    form = teachersubject()
    
    if request.method == 'POST':
        form = teachersubject(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showsubjects')
    else:
        form = teachersubject()

   
    context = {
        "form":form
    }

    return render(request, 'addsubject.html', context)

def updatesubject(request,pk):
    subject = subject.objects.get(id=pk)
    form = teachersubject(instance=product)
    
    if request.method == "POST":
        form = teachersubject(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('teachersubject')
        
    

    context = {
        "form":form
    }

    return render(request, 'updatesubject.html', context)

def deletesubject(request, pk):
    subject = subject.objects.get(id=pk)
    subject.delete()
    return redirect('teachersubject')





>>>>>>> 743cd069bdf10af63f6d89ae0d24ae8322a15528
