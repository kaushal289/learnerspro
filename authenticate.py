from django.shortcuts import redirect
from student.models import Student
from django.contrib import messages
class Authentication:
    def valid_user(function):
        def wrap(request):
            print(request)
            try:
                Student.objects.get(username=request.session['username'], password=request.session['password'])
                return function(request)
            except:
                print('no authentication')
            return redirect('/studentlogin')
        return wrap

    def valid_user_where_id(function):
        def wrap(request,p_id):
            try:
                Student.objects.get(username=request.session['username'], password=request.session['password'])
                return function(request,p_id)
            except:
                messages.warning(request, 'Please enter valid email and password')
                return redirect('/login')
        return wrap

