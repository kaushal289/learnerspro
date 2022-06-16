from django.shortcuts import render, redirect
from teacher.models import Teacher, Teachersubject
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
    return render(request,"teacher/landingpage.html")

def teachersubject(request):
    return render(request, "teacher/teachersubject.html")

def logout(request):
    request.session.clear()
    return redirect('/')


def addsubject(request):
    if request.method == "POST":
        form = teachersubject(request.POST, request.FILES)
        form.save()
        return redirect("/teachersubject")
    return render(request, "teacher/addsubject.html")

def teacherprofile(request,s_id):
    try:
        users=Teacher.objects.get(teacher_id=s_id)
        return render(request,"teacher/teacherprofile.html",{'users':[users]})
    except:
        print("No Data Found")
    return render(request,"Teacher/teacherprofile.html",{'users':[users]})

def teacherprofile(request,s_id):
    student=Teacher.objects.get(Teacher_id=s_id)
    if request.method=="POST":
        try:
            if len(request.FILES) != 0:
                if len(Teacher.image)>0:
                    os.remove(teacher.image.path)
                teacher.image=request.FILES['image']
        except:
            teacher.image=request.FILES['image']
    form=TeacherForm(request.POST, instance=Teacher)
    form.save()
    request.session['username']=request.POST['username']
    users=Teacher.objects.get(Teacher_id=s_id)
    return render(request,"teacher/teacherprofile.html",{'users':[users]})
